input_max_num = int(input("До какого числа сгенерировать нечетные числа?\n"))
odd_numbers = (number for number in range(1, input_max_num + 1, 2))
print(type(odd_numbers))

# for number in odd_numbers:
#     print(number)
# без StopIteration

while True:
    print(next(odd_numbers))
# с StopIteration
