cube_list = []
sum_numbers = 0
for numbers in range(1, 1000, 2):
    cube_list.append(numbers ** 3)
for numbers in cube_list:
    sum_number = 0
    numbers_copy = numbers
    while numbers_copy > 0:
        number = numbers_copy % 10
        sum_number = sum_number + number
        numbers_copy = numbers_copy // 10
    if sum_number % 7 == 0:
        sum_numbers = sum_numbers + numbers
print(sum_numbers)
sum_numbers = 0
for numbers in cube_list:
    sum_number = 0
    numbers_copy = numbers + 17
    while numbers_copy > 0:
        number = numbers_copy % 10
        sum_number = sum_number + number
        numbers_copy = numbers_copy // 10
    if sum_number % 7 == 0:
        sum_numbers = sum_numbers + (numbers + 17)
        # sum_numbers = sum_numbers + numbers           Если не правильно понял задание, то это второй вариант
print(sum_numbers)
