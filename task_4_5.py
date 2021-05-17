from utils import currency_rates


def main(argv):
    program, *args = argv
    currency_rates(*args)


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
