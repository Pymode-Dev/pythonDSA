"""
Quickselect is algorithm which relies on
partition and binary search.
"""


class QuickSelect:
    def __init__(self, array: list) -> None:
        self.array = array

    def _partition(self, left_pointer: int, right_pointer: int) -> int:
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
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], \
                    self.array[left_pointer]
                left_pointer += 1
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
        return left_pointer

    def quickselect(self, nth_lowest_value: int, left_index: int, right_index: int) -> int:
        if right_index - left_index <= 0:
            return self.array[left_index]

        pivot_index = self._partition(left_index, right_index)

        if nth_lowest_value < pivot_index:
            self.quickselect(nth_lowest_value, left_index, pivot_index - 1)
        elif nth_lowest_value > pivot_index:
            self.quickselect(nth_lowest_value, pivot_index + 1, right_index)
        elif pivot_index == nth_lowest_value:
            return self.array[pivot_index]


array = [0, 50, 20, 10, 60]
user = QuickSelect(array)
print(user.quickselect(1, 0, len(array) - 1))
