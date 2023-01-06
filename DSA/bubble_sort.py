"""This is a bubble sort implementation in Python."""


def bubble_sort(array: list) -> list:
    """
    Bubble Sort Algorithm.

    >>> bubble_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> bubble_sort([1, 2, 3, 4])
    [1, 2, 3, 4]
    """
    for index in range(len(array) - 1, 0, -1):
        for j in range(0, index):
            # if the current value is greater than the next one
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubble_sort([1, 2, 3, 4]))
