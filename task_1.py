num_dict = {
    "one": 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num):
    for key in num_dict.keys():
        if num == key:
            return num_dict.get(num)
    """
    Переберает ключи в словаре и возвращает значение подходящего.
    Если подходящего нет, возвращает None.
    
    :param num: Значение с которым сравнивает ключи.
    :return: Возвращаемое значение ключа или None.
    """


while True:
    num_input = input("Введи числительное на английском от 1 до 10 для перевода\n")
    if num_translate(num_input) != None:
        print(num_translate(num_input))
    else:
        print('Не соответствует условиям')

# Сделал циклом для удобства проверки и красоты
# Если перевод отсутствует возвращает None, но для красоты пишет о несоответствии исловиям.
