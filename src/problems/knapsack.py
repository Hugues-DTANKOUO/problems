"""
## Level: *`Medium`*

Imagine that you're a thief who has broken into a house.

You have a bag that can carry a maximum weight of `weight_capacity`.

You have to steal items from the house to maximize the total value of the items you steal.

Each item has a `weight` and a `value`.

The weight of the ith item is given by `weights[i]` and the value of the ith item is given by `values[i]`.

You can only take one of each item, and you can't take a fraction of an item.

Your goal is to maximize the total value of the items you steal,
but you can only carry at most `weight_capacity` weight.

Write a function that returns the maximum total value that you can steal.

## An Example:

Let's say that the `weight_capacity` is 50, and there are 3 items in the house.
The weights and values of the items are as follows:
- **weights** = [10, 20, 30]
- **values** = [60, 100, 120]

## You have six possible ways to steal items from the house:
- Steal the first item (weight = 10, value = 60)
- Steal the second item (weight = 20, value = 100)
- Steal the third item (weight = 30, value = 120)
- Steal the first and second items (total weight = 30, total value = 160)
- Steal the first and third items (total weight = 40, total value = 180)
- Steal the second and third items (total weight = 50, total value = 220)

The function should return **220**, which is the maximum total value that you can steal.

```bash
>knapsack --weight_capacity 50 --weights 10,20,30 --values 60,100,120
220
```
"""

# Import the necessary libraries here


def knapsack(weight_capacity: int, weights: list[int], values: list[int]) -> int:
    """
    Calculate the maximum total value that you can steal.

    :param weight_capacity: The maximum weight that the bag can carry.
    :param weights: The weights of the items.
    :param values: The values of the items.
    :return: The maximum total value that you can steal.
    """
    # Write your code here
    return ...  # type: ignore[return-value] # Replace this line with your code
