from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def max_jokes():
    '''

    Считает сколько шуток можно сложить из оставшихся слов в 3 списках.

    :return: Возвращает колличество возможных шуток.
    '''
    max_joke = len(nouns)
    if max_joke > len(adverbs):
        max_joke = len(adverbs)
    if max_joke > len(adjectives):
        max_joke = len(adjectives)
    return max_joke


def random_index(quantity_jokes):
    '''

    Выберает случайное слово из списка.

    :param quantity_jokes: Список из которого будет взято слово.
    :return: Возвращает индекс слова в списке
    '''
    i = randint(0, len(quantity_jokes) - 1)
    return i


def get_jokes(number, delete=False):
    '''

    Собирает шутки из 3 списков.

    :param number: Количество нужных шуток.
    :param delete: Нужно ли удалять использованные слова
    :return: Возвращает список с шутками.
    '''
    i = 0
    jokes = []
    while i < number:
        a = random_index(nouns)
        b = random_index(adverbs)
        c = random_index(adjectives)
        joke = f'{nouns[a]} {adverbs[b]} {adjectives[c]}'
        if delete == True:
            nouns.pop(a)
            adverbs.pop(b)
            adjectives.pop(c)
        jokes.append(joke)
        i += 1
    return jokes


quantity = int(input(f'Сколько шуток хочешь, максимум {max_jokes()}\n'))
while True:
    if max_jokes() > 0:
        if 0 < quantity <= max_jokes():
            print(get_jokes(quantity, True))  # Если убрать True, использованные слова не будут удаляться из списка
            if max_jokes() < 0:
                print(f'шутеек осталось: {max_jokes()}')
                quantity = int(input('Сколька нада?'))
        else:
            print(f'мне столько не выдать, максимум {max_jokes()}')
            quantity = int(input('Сколька нада?'))
    else:
        print('Шутки кончились ¯\(°_o)/¯')
        break

# Сделал почти максимально универсально. Можно добавлять в списки сколько угодно слов.
# Хотел сделать возможность задавать любые списки, и даже свои. По сути дело 3 секунд. но я чет упоролся и устал. (；一_一)
