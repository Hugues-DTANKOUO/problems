import importlib
import importlib.util

from pathlib import Path
from typing import Annotated, Any, Callable

from fastapi import Body, FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


CURRENT_DIR = Path(__file__).parent

app = FastAPI()


templates = Jinja2Templates(directory=CURRENT_DIR / "templates")

forbidden_words = [
    "os.",
    "sys.",
    "subprocess",
    "shutil",
    "importlib",
    "importlib.util",
    "__import__",
    "open",
    " as ",
    "sqlite3",
    "exec(",
    "eval(",
    "pickle",
    "marshal",
    "literal_eval",
]


with open(CURRENT_DIR / "anagram.py") as file:
    code = file.read()


@app.get("/solve/{problem_name}", response_class=HTMLResponse)
async def get_problem(request: Request, problem_name: str) -> Any:
    """
    Get the problem page with the code editor

    :param request: The request object
    :param problem_name: The name of the problem to solve
    :return: The problem page with the code editor
    """
    if not (CURRENT_DIR / f"{problem_name}.py").exists():
        return HTMLResponse(content="404 Not Found", status_code=404)

    problem_module = importlib.import_module(f"problems.{problem_name}")

    documentation = problem_module.__doc__ or ""

    # Get the code from the file
    with open(CURRENT_DIR / f"{problem_name}.py") as file:
        code = file.read()

    # Remove the documentation from the code and escape the backticks
    code = code.replace(f'"""{documentation}"""', "").lstrip().replace("`", r"\`")

    # Escape the backticks in the documentation
    documentation = documentation.replace("`", r"\`")

    # Render the problem page with the code editor and the documentation
    data = {"request": request, "code": code, "title": problem_name, "description": documentation}
    return templates.TemplateResponse("problem.html", data)


@app.post("/solve/{problem_name}")
async def solve(problem_name: str, data: Annotated[dict[str, str], Body(embed=False)]) -> dict[str, Any]:
    """
    Check the code provided by the user and run the tests

    :param problem_name: The name of the problem to solve
    :param data: The data from the form containing the code
    :return: The results of the tests
    """
    # Extract the code from the data
    code = data["code"]

    # Check if the code contains any forbidden words
    lower_code = code.lower()
    for word in forbidden_words:
        if word in lower_code:
            return {"error": f"You are not allowed to use the word '{word.replace('.', '').replace('(', '')}'"}

    # Execute the user's code in a restricted environment
    module_globals: dict[str, Any] = {}
    try:
        exec(code, module_globals)
    except Exception as e:
        return {"error": f"Invalid code. Execution error: {str(e)}"}

    # Look for the function in the user's code
    if problem_name not in module_globals:
        return {"error": "Do not change the function name"}
    user_function: Callable = module_globals[problem_name]

    # Load the original function from the problem module
    problem_module = importlib.import_module(f"problems.{problem_name}")
    original_function: Callable = getattr(problem_module, problem_name)

    # Compare the signature of the user's function with the original function
    if original_function.__annotations__ != user_function.__annotations__:
        return {"error": "The function signature is incorrect"}

    # Variable to store the results of the tests
    tests_result: list[str] = []

    # Load the test module for the problem and get the test functions
    test_module = importlib.import_module(f"problems.inside_test.{problem_name}_test")
    test_functions: list[Callable[[Callable], None]] = [
        getattr(test_module, function_name) for function_name in dir(test_module) if function_name.endswith("_test")
    ]

    # Run the tests for the user's function and store the results
    for test_index, test_function in enumerate(test_functions):
        try:
            test_function(user_function)
            tests_result.append(f"Test {test_index + 1}: Passed")
        except AssertionError as error:
            tests_result.append(f"Test {test_index + 1}: Failed - {str(error)}")

    return {"tests": tests_result}