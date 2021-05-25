# не смог сделать сам, по тому скопировал у тебя, каюсь, не отмечайте как сделанное, это чиста для себя
import math
import sys

line_lenght = 7


def show_sales(show_from_line=1, show_to_line=math.inf):
    if show_from_line < 2:
        show_from_position = 0
    else:
        show_from_position = (show_to_line - 1) * line_lenght

    show_to_position = show_to_line * line_lenght

    with open('bakery.csv', 'r', encoding='utf=8') as file:
        file.seek(show_from_position)
        line = file.readline()
        while line:
            print(line.strip())
            if show_to_position < file.tell():
                break
            line = file.readline()


if __name__ == '__main__':
    arguments = (int(arg) for arg in sys.argv[1:])
    show_sales(*arguments)
