list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_n = 0
max_i = 0

for index, number in enumerate(list_numbers):
    if number >= max_n:
        max_n = number
        max_i = index

list_numbers[-1], list_numbers[max_i] = max_n, list_numbers[-1]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

