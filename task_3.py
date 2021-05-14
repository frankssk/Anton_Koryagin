names_dict = {}
names_input = input("Введите имена через запятую\n")


def thesaurus(names, dict_parc):
    '''
    Приабразует из списка с именами словарь, ключами которого являются первые буквы имен,
    а также сортирует имена по ключам.
    :param names: список с именами
    :param dict_parc: словарь с которым работаем
    :return: возвращает готовый словарь
    '''
    names = names.split(', ')
    for name in names:
        key = name[0].capitalize()
        if key not in dict_parc:
            dict_parc[key] = []
        if key == name[0].capitalize():
            dict_parc[key].append(name)
    return dict_parc


print(thesaurus(names_input, names_dict))

print(dict(sorted(names_dict.items())))
# возвращаю отсортированный по ключам словарь

#  Макс Гриша Антон Анна
#  Макс, Гриша, Антон, Анна
