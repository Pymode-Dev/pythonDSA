"""Selection Sort implementation in Python."""


def selection_sort(array: list) -> list:
    """
    Selection Sort Algorithm.
    >>> selection_sort([9, 8, 7, 6, 5, 4])
    [4, 5, 6, 7, 8, 9]
    >>> selection_sort(["date", "cat", "ball", "apple"])
    ['apple', 'ball', 'cat', 'date']
    """
    for value in range(0, len(array) - 1):
        temp_lowest_value = value
        for j in range(value + 1, len(array)):
            if array[j] < array[temp_lowest_value]:
                temp_lowest_value = j
        if temp_lowest_value != value:
            temp = array[value]
            array[value] = array[temp_lowest_value]
            array[temp_lowest_value] = temp

    return array
