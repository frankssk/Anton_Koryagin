tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', "Женя", "Катя"]
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']


def generator_classes(list_1, list_2):
    '''

    Генерирует из 2 списков кортежи

    :param list_1: Первый список
    :param list_2: Второй список
    :return: Кориэжи
    '''
    for i in range(len(list_1)):
        if i < len(list_2):
            yield list_1[i], list_2[i]
        else:
            yield list_1[i], None


students_in_class = generator_classes(tutors, classes)
print(type(students_in_class))
# for students in students_in_class:
#     print(students)
# # без StopIteration
#
while True:
    print(next(students_in_class))
# # с StopIteration
