from typing import Callable, List

from problems.inside_test.util import async_timeout


async def nqueens_n4_test(func: Callable[[int], List[List[int]]]) -> None:
    """
    GIVEN n=4
    WHEN nqueens function is called
    THEN it should return valid solutions
    """
    _functional_nqueens = async_timeout(100)(func)
    solutions = await _functional_nqueens(4)
    assert isinstance(solutions, list), "Should return a list"
    assert len(solutions) > 0, "Should find at least one solution"
    assert all(is_valid_solution(4, sol) for sol in solutions), "All solutions should be valid"
    assert [1, 3, 0, 2] in solutions, "Should find the solution [1, 3, 0, 2]"


async def nqueens_n8_test(func: Callable[[int], List[List[int]]]) -> None:
    """
    GIVEN n=8
    WHEN nqueens function is called
    THEN it should return valid solutions
    """
    _functional_nqueens = async_timeout(5000)(func)
    solutions = await _functional_nqueens(8)
    assert isinstance(solutions, list), "Should return a list"
    assert len(solutions) > 0, "Should find at least one solution"
    assert all(is_valid_solution(8, sol) for sol in solutions), "All solutions should be valid"


async def nqueens_invalid_input_test(func: Callable[[int], List[List[int]]]) -> None:
    """
    GIVEN invalid input
    WHEN nqueens function is called
    THEN it should handle edge cases appropriately
    """
    _functional_nqueens = async_timeout(100)(func)

    solutions_n0 = await _functional_nqueens(0)
    assert isinstance(solutions_n0, list), "Should return a list"
    assert len(solutions_n0) == 0, "Should return empty list for n=0"

    solutions_n1 = await _functional_nqueens(1)
    assert isinstance(solutions_n1, list), "Should return a list"
    assert solutions_n1 == [[0]], "Should return [[0]] for n=1"

    solutions_n2 = await _functional_nqueens(2)
    assert isinstance(solutions_n2, list), "Should return a list"
    assert len(solutions_n2) == 0, "Should return empty list for n=2"

    solutions_n3 = await _functional_nqueens(3)
    assert isinstance(solutions_n3, list), "Should return a list"
    assert len(solutions_n3) == 0, "Should return empty list for n=3"


def is_valid_solution(n: int, solution: List[int]) -> bool:
    """
    Check if a solution is valid.

    :param n: Size of the board
    :param solution: Queen positions
    :return: True if valid, False otherwise
    """
    if len(solution) != n:
        return False

    # Check row and column conflicts
    if len(set(solution)) != n:
        return False

    # Check diagonal conflicts
    for i in range(n):
        for j in range(i + 1, n):
            if abs(solution[i] - solution[j]) == abs(i - j):
                return False

    return True
