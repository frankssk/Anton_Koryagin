while True:
    duration = int(input('Введите интересующий вас промежуток времени\n'))
    minute = duration // 60
    hour = minute // 60
    day = hour // 24
    month = day // 30.4  # взял среднее значение
    year = month // 12
    if duration < 60:
        print(f'{duration} сек.')
    elif minute < 60:
        print(f'{minute} мин. {duration % 60} сек.')
    elif hour < 24:
        print(f'{hour} час. {minute % 60} мин. {duration % 60} сек.')
    elif day < 30.44:
        print(f'{day} дн. {hour % 24} час. {minute % 60} мин. {duration % 60} сек.')
    elif month < 12:
        print(f'{int(month)} мес. {day % 30} дн. {hour % 24} час. {minute % 60} мин. {duration % 60} сек.')
    else:
        print(f'{int(year)} гд. {int(month) % 12} мес. {day % 30} дн. {hour % 24} час. {minute % 60} мин. {duration % 60} сек.')
