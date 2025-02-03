"""
## Level: *`Hard`*

The N Queens puzzle is the problem of placing N chess queens on an NxN chessboard
so that no two queens threaten each other. Thus, the solution requires that no two
queens share the same row, column, or diagonal.

## Example:

For N = 4, one possible solution is:
```
. Q . .
. . . Q
Q . . .
. . Q .
```

For N = 8, one possible solution is:
```
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. . . Q . . . .
. Q . . . . . .
```

## Function Signature:
```python
>nqueens(n=4)
[[1, 3, 0, 2]]  # List of valid queen placements
>nqueens(n=8)
[[0, 4, 7, 5, 2, 6, 1, 3]]  # One possible solution
```

## Notes:
- Return a list of valid solutions
- Each solution should be represented as a list of indices where queens are placed
- Time limit: 5 seconds
"""


def nqueens(n: int) -> list[list[int]]:
    """
    Solve the N Queens puzzle.

    :param n: Size of the board (NxN)
    :return: List of solutions where each solution is a list of queen positions
    """
    # Write your code here
    return ...  # type: ignore[return-value] # Replace this line with your code
