"""

"""


def get_largest_three_number(array: list) -> list:
    array: list = sorted(array)[-3:]
    return array


def multiply_three_largest_value():
    array = get_largest_three_number([9, 3, 2, 5, 6, 7, 1, 0, 4])

    product = 1
    for i in array:
        product *= i
    return product
