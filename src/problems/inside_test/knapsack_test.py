import json

from pathlib import Path
from typing import Callable

from problems.inside_test.util import async_timeout


DATA_PATH = Path(__file__).parent / "data" / "knapsack.jsonl"


async def knapsack_whithout_capacity_weight_then_return_0_test(
    func: Callable[[int, list[int], list[int]], int],
) -> None:
    """
    GIVEN a weight capacity of 0 and no items
    WHEN the function knapsack is called
    THEN it should return 0
    """
    _functional_knapsack = async_timeout(100)(func)

    assert await _functional_knapsack(0, [], []) == 0, "The function should return 0"

    assert await _functional_knapsack(0, [1, 2, 3], [1, 2, 3]) == 0, "The function should return 0"


async def knapsack_whithout_weight_and_values_then_return_0_test(
    func: Callable[[int, list[int], list[int]], int],
) -> None:
    """
    GIVEN a weight capacity and no items
    WHEN the function knapsack is called
    THEN it should return 0
    """
    _functional_knapsack = async_timeout(100)(func)

    assert await _functional_knapsack(10, [], []) == 0, "The function should return 0"


async def knapsack_with_one_item_and_capacity_weight_then_return_value_test(
    func: Callable[[int, list[int], list[int]], int],
) -> None:
    """
    GIVEN a weight capacity and one item
    WHEN the function knapsack is called
    THEN it should return the value of the item
    """
    _functional_knapsack = async_timeout(100)(func)

    assert await _functional_knapsack(10, [10], [10]) == 10, "The function should return 10"

    assert await _functional_knapsack(10, [10], [20]) == 20, "The function should return 20"

    assert await _functional_knapsack(15, [10], [20]) == 20, "The function should return 20"

    assert await _functional_knapsack(5, [10], [20]) == 0, "The function should return 0"


async def knapsack_with_two_items_and_capacity_weight_then_return_maximum_value_test(
    func: Callable[[int, list[int], list[int]], int],
) -> None:
    """
    GIVEN a weight capacity and two items
    WHEN the function knapsack is called
    THEN it should return the maximum value of the items
    """
    _functional_knapsack = async_timeout(100)(func)

    assert await _functional_knapsack(10, [10, 20], [10, 20]) == 10, "The function should return 10"

    assert await _functional_knapsack(10, [10, 20], [20, 30]) == 20, "The function should return 20"

    assert await _functional_knapsack(15, [10, 20], [20, 30]) == 20, "The function should return 20"

    assert await _functional_knapsack(5, [10, 20], [20, 30]) == 0, "The function should return 0"

    assert await _functional_knapsack(30, [10, 20], [20, 30]) == 50, "The function should return 50"

    assert (
        await _functional_knapsack(60, [10, 20, 30, 40], [60, 100, 120, 140]) == 280
    ), "The function should return 280"

    assert (
        await _functional_knapsack(50, [10, 20, 30, 40], [60, 100, 120, 140]) == 220
    ), "The function should return 220"


async def knapsack_with_large_items_and_capacity_weight_then_return_maximum_value_test(
    func: Callable[[int, list[int], list[int]], int],
) -> None:
    """
    GIVEN a weight capacity and large items
    WHEN the function knapsack is called
    THEN it should return the maximum value of the items
    """
    _functional_knapsack = async_timeout(5000)(func)

    with open(DATA_PATH) as file:
        items = file.readlines()
        for item in items:
            data = json.loads(item)
            weight_capacity = data["weight_capacity"]
            weights = data["weights"]
            values = data["values"]
            assert (
                await _functional_knapsack(weight_capacity, weights, values) == data["maximum_value"]
            ), f"The function should return {data['maximum_value']}"
