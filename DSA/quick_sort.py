"""
QuickSort is an Algorithm that use the concept of
partitioning and recursion.
We first partition the unsorted, and we apply recursive function
on the partitioned array.
"""


class QuickSort:
    """
    QuickSort Class
    """

    def __init__(self, array: list) -> None:
        self.array = array

    def _partition(self, left_pointer: int, right_pointer: int) -> int:
        """
        The module that handles the partition
        :param left_pointer:
        :param right_pointer:
        :return: left_pointer: int
        """
        pivot_index = right_pointer
        pivot_value = self.array[pivot_index]

        right_pointer -= 1

        while True:
            while self.array[left_pointer] < pivot_value:
                left_pointer += 1

            while self.array[right_pointer] > pivot_value:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[
                    left_pointer]
                left_pointer += 1
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
        return left_pointer

    def quicksort(self, left_index: int, right_index: int) -> list:
        """
        quicksort module which handles recursion to the left, and right
        of the partitioned array.
        :param left_index:
        :param right_index:
        :return: self.array: list
        """
        if right_index - left_index <= 0:
            return None

        pivot = self._partition(left_index, right_index)
        self.quicksort(left_index, pivot - 1)
        self.quicksort(pivot + 1, right_index)

        return self.array
