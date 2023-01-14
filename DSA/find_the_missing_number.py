"""
The following function finds the “missing number” from an array of integers. That is, the array is expected to have all integers from 0 up to the
array’s length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is
missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the
number 8.
"""


def arrange_the_array(array: list):
    arranged_array = set(sorted(array))
    original_array = set(range(0, len(arranged_array)))

    return original_array - arranged_array
