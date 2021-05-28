import os
from pathlib import Path as ph

file_statistic_not_tuple = {'10': [0, []], '100': [0, []], '1000': [0, []], '10000': [0, []], '100000': [0, []]}
file_statistic_tuple = {'10': (), '100': (), '1000': (), '10000': (), '100000': ()}


def file_type(file):
    type_f = ph(file).suffix
    return type_f


def append_to_dict(file_size, key):
    file_statistic_not_tuple[key][0] += 1
    type_f = file_type(file_size)
    if type_f not in file_statistic_not_tuple[key][1]:
        file_statistic_not_tuple[key][1].append(file_type(file_size))


def file_size(file_to_size):
    if 0 <= os.path.getsize(file_to_size) <= 10:
        append_to_dict(file_to_size, '10')
    elif 10 < os.path.getsize(file_to_size) <= 10 ** 2:
        append_to_dict(file_to_size, '100')
    elif 10 ** 2 < os.path.getsize(file_to_size) <= 10 ** 3:
        append_to_dict(file_to_size, '1000')
    elif 10 ** 3 < os.path.getsize(file_to_size) <= 10 ** 4:
        append_to_dict(file_to_size, '10000')
    elif 10 ** 4 < os.path.getsize(file_to_size) <= 10 ** 5:
        append_to_dict(file_to_size, '100000')


def file_or_not(file_name, file_directory):
    if os.path.isfile(f'{file_directory}/{file_name}'):
        file_size(f'{file_directory}/{file_name}')


def file_to_dict(file_directory):
    for file in os.listdir(file_directory):
        file_or_not(file, file_directory)


def dict_tuple():
    for key in file_statistic_tuple:
        file_statistic_tuple[key] = file_statistic_not_tuple[key][0], file_statistic_not_tuple[key][1]


def write_to_file(file_directory):
    name_file = os.path.basename(file_directory)
    os.chdir(file_directory)
    with open(f'{name_file}_summary.json', 'w', encoding='utf=8') as f:
        f.write(str(file_statistic_tuple))


def main():
    file_dir = input('Введите путь к директории для вывода статистики по размерам файлов\n')
    try:
        file_to_dict(file_dir)
    except FileNotFoundError:
        print('Путь не является директорией или его не существует')
        exit(main())
    dict_tuple()
    write_to_file(file_dir)
    print(file_statistic_tuple)


if __name__ == '__main__':
    main()
