while True:
    number = int(input('Введите число от 1 до 20\n'))
    if number == 1:
        print(f'{number} процент')
    elif 2 <= number <= 4:
        print(f'{number} процена')
    elif 5 <= number <= 20:
        print(f'{number} проценов')
    else:
        print('не верный запрос')
