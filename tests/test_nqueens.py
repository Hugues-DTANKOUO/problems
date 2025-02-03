import pytest

from problems.inside_test import nqueens_test
from problems.nqueens import nqueens


def correct_nqueens(n: int) -> list[list[int]]:
    """
    Solve the N Queens puzzle.

    :param n: Size of the board (NxN)
    :return: List of solutions where each solution is a list of queen positions
    """

    def is_safe(board: list[int], row: int, col: int) -> bool:
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def solve(board: list[int], row: int) -> None:
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions: list[list[int]] = []
    if n <= 0:
        return []
    if n == 1:
        return [[0]]
    if n in [2, 3]:
        return []

    solve([-1] * n, 0)
    return solutions


async def test_test_case_with_n4_and_base_function_then_error() -> None:
    """
    GIVEN a test case with n=4 and base function
    WHEN nqueens function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="Should return a list"):
        await nqueens_test.nqueens_n4_test(nqueens)


async def test_test_case_with_n4_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with n=4 and correct function
    WHEN nqueens function is called
    THEN any error should not be raised
    """
    await nqueens_test.nqueens_n4_test(correct_nqueens)


async def test_test_case_with_n8_and_base_function_then_error() -> None:
    """
    GIVEN a test case with n=8 and base function
    WHEN nqueens function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="Should return a list"):
        await nqueens_test.nqueens_n8_test(nqueens)


async def test_test_case_with_n8_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with n=8 and correct function
    WHEN nqueens function is called
    THEN any error should not be raised
    """
    await nqueens_test.nqueens_n8_test(correct_nqueens)


async def test_test_case_with_invalid_input_and_base_function_then_error() -> None:
    """
    GIVEN a test case with invalid input and base function
    WHEN nqueens function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="Should return a list"):
        await nqueens_test.nqueens_invalid_input_test(nqueens)


async def test_test_case_with_invalid_input_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with invalid input and correct function
    WHEN nqueens function is called
    THEN any error should not be raised
    """
    await nqueens_test.nqueens_invalid_input_test(correct_nqueens)


async def test_test_case_with_n8_and_slow_correct_function_then_error() -> None:
    """
    GIVEN a test case with n=8 and slow correct function
    WHEN nqueens function is called
    THEN an AssertionError should be raised
    """

    def slow_correct_nqueens(n: int) -> list[list[int]]:
        import time

        time.sleep(5)
        return correct_nqueens(n)

    with pytest.raises(AssertionError, match="Function timed out after 5000 milliseconds"):
        await nqueens_test.nqueens_n8_test(slow_correct_nqueens)
