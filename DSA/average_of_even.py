def average_of_even(array: list) -> float:
    total = 0
    count_of_even_numbers = 0

    for number in array:
        if number % 2 == 0:
            total += number
            count_of_even_numbers += 1

    return total/count_of_even_numbers


print(average_of_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
