def generation_number(max_num):
    '''

    Генератон нечетных чисел.

    :param max_num: До какого числа генерировать.
    :return: Нечетные числа.
    '''
    for num in range(1, max_num + 1, 2):
        yield num


input_max_num = int(input("До какого числа сгенерировать нечетные числа?\n"))
odd_numbers = generation_number(input_max_num)
print(type(odd_numbers))

# for number in odd_numbers:
#     print(number)
# без StopIteration

while True:
    print(next(odd_numbers))
# с StopIteration
