import subprocess

from pathlib import Path


path = Path(__file__).parent


def run_lint() -> None:
    """Run ruff format, ruff check and mypy."""

    print("Running ruff format")
    subprocess.run(["ruff", "format", path], check=True)
    print("Running ruff format on tests directory")
    subprocess.run(["ruff", "format", path.parents[1] / "tests"], check=True)

    print("Running ruff check")
    subprocess.run(["ruff", "check", path, "--fix"], check=True)
    print("Running ruff check on tests directory")
    subprocess.run(["ruff", "check", path.parents[1] / "tests", "--fix"], check=True)

    print("Running mypy")
    subprocess.run(["mypy", path], check=True)
    print("Running mypy on tests directory")
    subprocess.run(["mypy", path.parents[1] / "tests"], check=True)


def run_tests() -> None:
    """Run pytest."""
    print("Running pytest")
    subprocess.run(
        [
            "pytest",
            path.parents[1] / "tests",
            "-v",
        ],
    )


def run_all_checks() -> None:
    """Run all checks."""
    run_lint()
    run_tests()


def run_server() -> None:
    """Run the fastapi server."""
    print("Running the fastapi server")
    subprocess.run(["uvicorn", "problems.interface:app", "--reload"], check=True)
