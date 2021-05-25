# не смог сделать сам, по тому скопировал у тебя, каюсь, не отмечайте как сделанное, это чиста для себя
import sys


def add_sale(record_to_add):
    with open('bakery.csv', 'a', encoding='utf=8') as file:
        file.write(f'{record_to_add}\n')


if __name__ == '__main__':
    program, price_rec = sys.argv
    add_sale(price_rec)
