from problems.inside_test import knapsack_test
from problems.knapsack import knapsack


def test_knapsack_whithout_capacity_weight_then_return_0() -> None:
    """
    GIVEN a weight capacity of 0 and no items
    WHEN the function knapsack is called
    THEN it should return 0
    """
    knapsack_test.knapsack_whithout_capacity_weight_then_return_0_test(knapsack)


def test_knapsack_whithout_weight_and_values_then_return_0() -> None:
    """
    GIVEN a weight capacity and no items
    WHEN the function knapsack is called
    THEN it should return 0
    """
    knapsack_test.knapsack_whithout_weight_and_values_then_return_0_test(knapsack)


def test_knapsack_with_one_item_and_capacity_weight_then_return_value() -> None:
    """
    GIVEN a weight capacity and one item
    WHEN the function knapsack is called
    THEN it should return the value of the item
    """
    knapsack_test.knapsack_with_one_item_and_capacity_weight_then_return_value_test(knapsack)


def test_knapsack_with_two_items_and_capacity_weight_then_return_maximum_value() -> None:
    """
    GIVEN a weight capacity and two items
    WHEN the function knapsack is called
    THEN it should return the maximum value of the items
    """
    knapsack_test.knapsack_with_two_items_and_capacity_weight_then_return_maximum_value_test(knapsack)


def test_knapsack_with_large_items_and_capacity_weight_then_return_maximum_value() -> None:
    """
    GIVEN a weight capacity and large items
    WHEN the function knapsack is called
    THEN it should return the maximum value of the items
    """
    knapsack_test.knapsack_with_large_items_and_capacity_weight_then_return_maximum_value_test(knapsack)
