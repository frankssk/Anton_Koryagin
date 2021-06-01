import re


def email_parse(email_address):
    parsed = re.findall(r'([^@]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$', email_address)
    if not parsed:
        raise ValueError(f"Не верный email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))


def main():
    email_input = input('Введите email:\n')
    email_dict = email_parse(email_input)
    print(email_dict)


if __name__ == '__main__':
    main()
