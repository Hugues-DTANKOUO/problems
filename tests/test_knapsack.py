from pathlib import Path
from problems.knapsack import knapsack
import functools
from unittest import mock
from time import time
from typing import Callable
import json

DATA_PATH = Path(__file__).parent / "data" / "knapsack.jsonl"


def _non_functional_check(
    func: Callable[[int, list[int], list[int]], int],
) -> Callable[[int, list[int], list[int]], int]:
    """
    A decorator that checks if the function knpasack is implemented correctly.

    The function should not use the lru_cache decorator or implement its own caching mechanism.

    :param func: The function to check
    :return: The wrapper function
    """

    def check_cache_usage(
        func2: Callable[[int, list[int], list[int]], int],
    ) -> Callable[[int, list[int], list[int]], int]:
        """
        An internal decorator that checks if the function uses the lru_cache decorator.

        :param func2: The function to check
        :return: The wrapper function
        """

        def wrapper(weight_capacity: int, weights: list[int], values: list[int]) -> int:
            try:
                with mock.patch("problems.knapsack.lru_cache", side_effect=functools.lru_cache) as mock_lru_cache:
                    result = func2(weight_capacity, weights, values)
                    count_lru_cache = mock_lru_cache.call_count
                    assert count_lru_cache == 0, f"lru_cache() was called {count_lru_cache} times, please do not use it"
                    return result
            except AttributeError as error:
                if "does not have the attribute 'lru_cache'" in str(error):
                    return func2(weight_capacity, weights, values)
                raise error

        return wrapper

    @check_cache_usage
    def wrapper(weight_capacity: int, weights: list[int], values: list[int]) -> int:
        start_time = time()
        result = func(weight_capacity, weights, values)
        duration = time() - start_time
        assert duration < 5, f"The function is too slow ({duration:.5f} seconds)"
        return result

    return wrapper


_functional_knapsack = _non_functional_check(knapsack)


def test_knapsack_whithout_capacity_weight_then_return_0() -> None:
    """
    GIVEN a weight capacity of 0 and no items
    WHEN the function knapsack is called
    THEN it should return 0
    """
    assert _functional_knapsack(0, [], []) == 0

    assert _functional_knapsack(0, [1, 2, 3], [1, 2, 3]) == 0


def test_knapsack_whithout_weight_and_values_then_return_0() -> None:
    """
    GIVEN a weight capacity and no items
    WHEN the function knapsack is called
    THEN it should return 0
    """
    assert _functional_knapsack(10, [], []) == 0


def test_knapsack_with_one_item_and_capacity_weight_then_return_value() -> None:
    """
    GIVEN a weight capacity and one item
    WHEN the function knapsack is called
    THEN it should return the value of the item
    """
    assert _functional_knapsack(10, [10], [10]) == 10

    assert _functional_knapsack(10, [10], [20]) == 20

    assert _functional_knapsack(15, [10], [20]) == 20

    assert _functional_knapsack(5, [10], [20]) == 0


def test_knapsack_with_two_items_and_capacity_weight_then_return_maximum_value() -> None:
    """
    GIVEN a weight capacity and two items
    WHEN the function knapsack is called
    THEN it should return the maximum value of the items
    """
    assert _functional_knapsack(10, [10, 20], [10, 20]) == 10

    assert _functional_knapsack(10, [10, 20], [20, 30]) == 20

    assert _functional_knapsack(15, [10, 20], [20, 30]) == 20

    assert _functional_knapsack(5, [10, 20], [20, 30]) == 0

    assert _functional_knapsack(30, [10, 20], [20, 30]) == 50

    assert _functional_knapsack(60, [10, 20, 30, 40], [60, 100, 120, 140]) == 280

    assert _functional_knapsack(50, [10, 20, 30, 40], [60, 100, 120, 140]) == 220


def test_knapsack_with_large_items_and_capacity_weight_then_return_maximum_value() -> None:
    """
    GIVEN a weight capacity and large items
    WHEN the function knapsack is called
    THEN it should return the maximum value of the items
    """
    with open(DATA_PATH) as file:
        items = file.readlines()
        for item in items:
            data = json.loads(item)
            weight_capacity = data["weight_capacity"]
            weights = data["weights"]
            values = data["values"]
            assert _functional_knapsack(weight_capacity, weights, values) == data["maximum_value"]
