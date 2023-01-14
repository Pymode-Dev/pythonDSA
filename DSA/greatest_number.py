"""
Write three different implementations of a function that finds the greatest
number within an array. Write one function that is O(N2), one that is O(N
log N), and one that is O(N).
"""


def search_with_nth_step(array: list) -> int:
    greatest = 0

    for i in array:
        if i > greatest:
            greatest = i

    return greatest


def search_with_nlogn_step(array: list) -> int:
    """
    Since will know that the largest will be at the back
    when sorted.
    :param array:
    :return:
    """
    return sorted(array)[-1]
