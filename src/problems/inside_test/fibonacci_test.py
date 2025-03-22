from typing import Callable

from problems.inside_test.util import async_timeout


async def fibonacci_base_cases_test(fibonacci_func: Callable[[int], int]) -> None:
    """
    GIVEN base cases (0 and 1)
    WHEN fibonacci function is called
    THEN it should return correct values
    """
    _functional_fibonacci = async_timeout(100)(fibonacci_func)

    assert await _functional_fibonacci(0) == 0, "F(0) should be 0"
    assert await _functional_fibonacci(1) == 1, "F(1) should be 1"


async def fibonacci_small_values_test(fibonacci_func: Callable[[int], int]) -> None:
    """
    GIVEN small input values
    WHEN fibonacci function is called
    THEN it should return correct values
    """
    _functional_fibonacci = async_timeout(100)(fibonacci_func)

    assert await _functional_fibonacci(2) == 1, "F(2) should be 1"
    assert await _functional_fibonacci(6) == 8, "F(6) should be 8"


async def fibonacci_medium_value_test(fibonacci_func: Callable[[int], int]) -> None:
    """
    GIVEN a medium input value
    WHEN fibonacci function is called
    THEN it should return correct value within timeout
    """
    _functional_fibonacci = async_timeout(1000)(fibonacci_func)

    assert await _functional_fibonacci(20) == 6765, "F(20) should be 6765"


async def fibonacci_large_value_test(fibonacci_func: Callable[[int], int]) -> None:
    """
    GIVEN a large input value
    WHEN fibonacci function is called
    THEN it should return correct value within timeout
    """
    _functional_fibonacci = async_timeout(5000)(fibonacci_func)

    assert await _functional_fibonacci(35) == 9227465, "F(35) should be 9227465"


async def fibonacci_invalid_input_test(fibonacci_func: Callable[[int], int]) -> None:
    """
    GIVEN invalid inputs
    WHEN fibonacci function is called
    THEN it should raise appropriate exceptions
    """
    _functional_fibonacci = async_timeout(100)(fibonacci_func)

    try:
        await _functional_fibonacci(-1)
        raise AssertionError("Negative input should raise ValueError")
    except ValueError:
        pass

    try:
        await _functional_fibonacci(1.5)
        raise AssertionError("Non-integer input should raise TypeError")
    except TypeError:
        pass
