from functools import lru_cache
from time import sleep

import pytest

from problems.fibonacci import fibonacci
from problems.inside_test import fibonacci_test


@lru_cache(maxsize=None)
def correct_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    The Fibonacci sequence starts with 0 and 1, with each subsequent number
    being the sum of the two preceding ones.

    :param n: A non-negative integer
    :return: The nth Fibonacci number
    """
    # check if input is valid
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case with memoization handled by @lru_cache
    return correct_fibonacci(n - 1) + correct_fibonacci(n - 2)


async def test_test_case_with_base_cases_and_base_function_then_error() -> None:
    """
    GIVEN a test case with base cases and base function
    WHEN the fibonacci function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="F\\(0\\) should be 0"):
        await fibonacci_test.fibonacci_base_cases_test(fibonacci)


async def test_test_case_with_base_cases_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with base cases and correct function
    WHEN the fibonacci function is called
    THEN any error should not be raised
    """
    await fibonacci_test.fibonacci_base_cases_test(correct_fibonacci)


async def test_test_case_with_small_values_and_base_function_then_error() -> None:
    """
    GIVEN a test case with small values and base function
    WHEN the fibonacci function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="F\\(2\\) should be 1"):
        await fibonacci_test.fibonacci_small_values_test(fibonacci)


async def test_test_case_with_small_values_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with small values and correct function
    WHEN the fibonacci function is called
    THEN any error should not be raised
    """
    await fibonacci_test.fibonacci_small_values_test(correct_fibonacci)


async def test_test_case_with_medium_value_and_base_function_then_error() -> None:
    """
    GIVEN a test case with medium value and base function
    WHEN the fibonacci function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="F\\(20\\) should be 6765"):
        await fibonacci_test.fibonacci_medium_value_test(fibonacci)


async def test_test_case_with_medium_value_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with medium value and correct function
    WHEN the fibonacci function is called
    THEN any error should not be raised
    """
    await fibonacci_test.fibonacci_medium_value_test(correct_fibonacci)


async def test_test_case_with_large_value_and_base_function_then_error() -> None:
    """
    GIVEN a test case with large value and base function
    WHEN the fibonacci function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="F\\(35\\) should be 9227465"):
        await fibonacci_test.fibonacci_large_value_test(fibonacci)


async def test_test_case_with_large_value_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with large value and correct function
    WHEN the fibonacci function is called
    THEN any error should not be raised
    """
    await fibonacci_test.fibonacci_large_value_test(correct_fibonacci)


async def test_test_case_with_invalid_input_and_base_function_then_error() -> None:
    """
    GIVEN a test case with invalid input and base function
    WHEN the fibonacci function is called
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="Negative input should raise ValueError"):
        await fibonacci_test.fibonacci_invalid_input_test(fibonacci)


async def test_test_case_with_invalid_input_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with invalid input and correct function
    WHEN the fibonacci function is called
    THEN any error should not be raised
    """
    await fibonacci_test.fibonacci_invalid_input_test(correct_fibonacci)


async def test_test_case_with_large_value_and_slow_correct_function_then_error() -> None:
    """
    GIVEN a test case with large value and slow correct function
    WHEN the fibonacci function is called
    THEN an AssertionError should be raised
    """

    def slow_fibonacci(n: int) -> int:
        """Slow implementation of fibonacci with artificial delay."""
        sleep(5)
        return correct_fibonacci(n)

    with pytest.raises(AssertionError, match="Function timed out after 5000 milliseconds"):
        await fibonacci_test.fibonacci_large_value_test(slow_fibonacci)
