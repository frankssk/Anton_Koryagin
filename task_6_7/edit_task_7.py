# не смог сделать сам, по тому скопировал у тебя, каюсь, не отмечайте как сделанное, это чиста для себя
import sys

line_length = 7


def edit_sales(line_from, new_rec):
    line_from -= 1
    with open('bakery.csv', 'r+', encoding='utf=8') as file:
        file.seek(line_from * line_length)
        if not file.readline():
            print('Записи не существует')
            return
        file.seek(line_from * line_length)
        file.write(new_rec)


if __name__ == '__main__':
    program, edit_from_line_from, new_rec = sys.argv
    edit_sales(int(edit_from_line_from), new_rec)
