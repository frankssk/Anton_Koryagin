names_dict = {}
names_input = input('Введите имя фамилия через запитую.\n')


def thesaurus_adv(names_surnames, dict_parc):
    '''
    Приабразует из списка с именами и фамилиями словарь, ключами которого являются первые буквы фамилии,
    в которых еще словарь с ключами по первой букве имени.
    :param names_surnames: список с именами и фамилиями.
    :param dict_parc: словарь с которым работаем.
    :return: возвращает готовый словарь.
    '''
    names_surnames = names_surnames.split(', ')
    for surname in names_surnames:
        surname = surname.split(' ')
        key = surname[1][0].capitalize()
        if key not in dict_parc:
            dict_parc[key] = {}
        if key == surname[1][0].capitalize():
            surname = ' '.join(surname)
            dict_parc[key].fromkeys(thesaurus(dict_parc[key], surname))
    return dict_parc


def thesaurus(dict_parc, names):
    '''
    Приабразует из списка с именами и фамилиями словарь, ключами которого являются первые буквы имен.
    :param names: список с именами и фамилиями.
    :param dict_parc: словарь с которым работаем.
    :return: возвращает готовый словарь.
    '''
    key = names[0].capitalize()
    if key not in dict_parc:
        dict_parc[key] = []
    if key == names[0].capitalize():
        dict_parc[key].append(names)
    return dict_parc


print(thesaurus_adv(names_input, names_dict))

print(dict(sorted(names_dict.items())))
# возвращаю отсортированный по ключам словарь

#  Макс Кукушкин, Гриша клюев, Антон васерман, Анна петрушка
