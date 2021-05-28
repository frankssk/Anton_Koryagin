import os


def make_dir(name_dir):
    try:
        os.makedirs(name_dir)
    except FileExistsError:
        print(f'Папка {name_dir} уже существует')


def quantity_folder(in_dir):
    while True:
        try:
            if in_dir == os.getcwd():
                print(f'Вы в дериктории {os.getcwd()}')
                quantity_dir = int(input("Сколько директорий вам нужно?\n"))
            else:
                quantity_dir = int(input("Сколько папок вам нужно?\n"))
            return quantity_dir
        except ValueError:
            print('Введите число')


def make_folder(in_dir):
    i = 1
    folder = quantity_folder(in_dir)
    while i <= folder:
        name_dir = input(f"Введите название {i} папки\n")
        try:
            os.makedirs(name_dir)
            i += 1
        except FileExistsError:
            print(f'Папка {name_dir} уже существует')


def top_dir():
    while True:
        name_top_dir = input("Введите название директории\n")
        try:
            make_dir(name_top_dir)
            return name_top_dir
        except FileExistsError:
            print(f'Папка {name_top_dir} уже существует')


def quantity_top_dir():
    i = 1
    main_dir = os.getcwd()
    folder = quantity_folder(main_dir)
    while i <= folder:
        os.chdir(top_dir())
        print(f'Вы в дериктории {os.getcwd()}')
        make_folder(main_dir)
        os.chdir(main_dir)
        i += 1


# простенький вариант с коленки
def main():
    make_dir('my_project')
    os.chdir('my_project')
    make_dir('settings')
    make_dir('mainapp')
    make_dir('adminapp')
    make_dir('authapp')


if __name__ == '__main__':
    main()

# универсальный вариант
#
# def main():
#     quantity_top_dir()
#
#
# if __name__ == '__main__':
#     main()
