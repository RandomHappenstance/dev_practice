"""
    All The Project Euler archive problems.
"""


def mult_sum(value: int) -> int:
    """ Problem 1.

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    Returns:
        object:
    """

    def three_or_five(val) -> bool:
        if val % 3 == 0 or val % 5 == 0:
            return True
        else:
            return False

    total = 0
    for num in range(0, value):
        if three_or_five(num):
            total += num

    return total