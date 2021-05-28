import os

dir_log_index = []


def make_dir(name_dir):
    try:
        os.makedirs(name_dir)
    except FileExistsError:
        print(f'Папка {name_dir} уже существует')


def make_file(name_file, type_file):
    try:
        f = open(f'{name_file}.{type_file}', 'x')
        f.close()
    except FileExistsError:
        print(f'файл {name_file}.{type_file} уже существует')


def split_dir(file_to_split):
    for list in file_to_split:
        dir_list = list.strip('\n')
        dir_list = dir_list.split('--')
        dir_index = dir_list.pop(0)
        dir_index = dir_index.replace(' ', '_')
        dir_list = dir_list[0].split('.')
        dir_name = dir_list[0]
        try:
            file_type = dir_list[1]
        except IndexError:
            file_type = None
        yield dir_index, dir_name, file_type


def make_dir_tree(dir_log):
    dir_index, dir_name, file_type = dir_log
    while True:
        if dir_index not in dir_log_index:
            dir_log_index.append(dir_index)
            if file_type == None:
                make_dir(dir_name)
                os.chdir(dir_name)
                break
            elif file_type != None:
                make_file(dir_name, file_type)
                dir_log_index.pop()
                break
        else:
            dir_log_index.pop()
            os.chdir('..')


def open_conf():
    with open('config.yaml', 'r', encoding='utf=8') as file:
        for dir_log in split_dir(file):
            make_dir_tree(dir_log)


if __name__ == '__main__':
    open_conf()
