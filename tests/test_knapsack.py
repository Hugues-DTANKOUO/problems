import pytest

from problems.inside_test import knapsack_test
from problems.knapsack import knapsack


def correct_knapsack(weight_capacity: int, weights: list[int], values: list[int]) -> int:
    """
    Calculate the maximum value that can be obtained by selecting items
    with a weight less than or equal to the capacity.

    :param weight_capacity: The weight capacity of the knapsack.
    :param weights: The weights of the items.
    :param values: The values of the items.
    :return: The maximum value that can be obtained.
    """

    n = len(weights)
    dp = [[0] * (weight_capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, weight_capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][weight_capacity]


async def test_test_case_with_capacity_weight_0_and_base_function_then_error() -> None:
    """
    GIVEN a test case with a weight capacity of 0, no items and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The function should return 0"):
        await knapsack_test.knapsack_whithout_capacity_weight_then_return_0_test(knapsack)


async def test_test_case_with_capacity_weight_0_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with a weight capacity of 0, no items and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await knapsack_test.knapsack_whithout_capacity_weight_then_return_0_test(correct_knapsack)


async def test_test_case_with_no_weight_and_values_and_base_function_then_error() -> None:
    """
    GIVEN a test case with a weight capacity, no items and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The function should return 0"):
        await knapsack_test.knapsack_whithout_weight_and_values_then_return_0_test(knapsack)


async def test_test_case_with_no_weight_and_values_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with a weight capacity, no items and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await knapsack_test.knapsack_whithout_weight_and_values_then_return_0_test(correct_knapsack)


async def test_test_case_with_one_item_and_capacity_weight_and_base_function_then_error() -> None:
    """
    GIVEN a test case with a weight capacity, one item and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The function should return 10"):
        await knapsack_test.knapsack_with_one_item_and_capacity_weight_then_return_value_test(knapsack)


async def test_test_case_with_one_item_and_capacity_weight_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with a weight capacity, one item and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await knapsack_test.knapsack_with_one_item_and_capacity_weight_then_return_value_test(correct_knapsack)


async def test_test_case_with_two_items_and_capacity_weight_and_base_function_then_error() -> None:
    """
    GIVEN a test case with a weight capacity, two items and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The function should return 10"):
        await knapsack_test.knapsack_with_two_items_and_capacity_weight_then_return_maximum_value_test(knapsack)


async def test_test_case_with_two_items_and_capacity_weight_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with a weight capacity, two items and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await knapsack_test.knapsack_with_two_items_and_capacity_weight_then_return_maximum_value_test(correct_knapsack)


async def test_test_case_with_large_items_and_capacity_weight_and_base_function_then_error() -> None:
    """
    GIVEN a test case with a weight capacity, large items and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The function should return 13186"):
        await knapsack_test.knapsack_with_large_items_and_capacity_weight_then_return_maximum_value_test(knapsack)


async def test_test_case_with_large_items_and_capacity_weight_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with a weight capacity, large items and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await knapsack_test.knapsack_with_large_items_and_capacity_weight_then_return_maximum_value_test(correct_knapsack)


async def test_test_case_with_large_items_and_capacity_weight_and_slow_correct_function_then_error() -> None:
    """
    GIVEN a test case with a weight capacity, large items and slow correct function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """

    def slow_correct_knapsack(weight_capacity: int, weights: list[int], values: list[int]) -> int:
        import time

        time.sleep(5)

        return correct_knapsack(weight_capacity, weights, values)

    with pytest.raises(AssertionError, match="Function timed out after 5000 milliseconds"):
        await knapsack_test.knapsack_with_large_items_and_capacity_weight_then_return_maximum_value_test(
            slow_correct_knapsack
        )
