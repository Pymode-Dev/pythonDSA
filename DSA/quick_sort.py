"""
Quicksort is a sorting algorithm which consist of two concepts:
partition and quicksort itself.
"""


class QuickSort:
    """
    Quicksort Class
    """

    def __init__(self, array: list) -> None:
        self.array = array

    def _partition(self, left_pointer: int, right_pointer: int) -> int:
        """
        We firstly partition the array before sorting.
        :param left_pointer:
        :param right_pointer:
        :return: int

        >>> array = [5, 0, 2, 1, 4, 6, 3]
        >>> user = QuickSort(array)
        >>> user._partition(0, len(array) - 1)
        3
        """
        pivot_index = right_pointer
        pivot = self.array[pivot_index]

        right_pointer -= 1

        while True:
            while self.array[left_pointer] < pivot:
                left_pointer += 1

            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], \
                    self.array[left_pointer]
                left_pointer += 1
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
        return left_pointer

    def quicksort(self, left_index: int, right_index: int) -> list:
        """
        Now we sort the partitioned array:
        1. first to the left and,
        2. to the right
        :param left_index:
        :param right_index:
        :return: list

        array = [5, 0, 2, 1, 4, 6, 3]
        user = QuickSort(array)
        user.quicksort(0, len(array) - 1)
        [0, 1, 2, 3, 4, 5, 6]
        """
        if right_index - left_index <= 0:
            return None

        pivot_index = self._partition(left_index, right_index)
        self.quicksort(left_index, pivot_index - 1)
        self.quicksort(pivot_index + 1, right_index)

        return self.array
