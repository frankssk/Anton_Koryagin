import sys
from itertools import zip_longest


def users_and_hobbies(users_file, hobbies_file, out_file):
    with open(users_file, 'r', encoding='utf=8') as users_f, \
            open(hobbies_file, 'r', encoding='utf=8') as hobbies_f, \
            open(out_file, 'a', encoding='utf=8') as out_f:
        for users, hobbies in zip_longest(users_f, hobbies_f):
            if users is None:
                exit(1)
            else:
                users = users.strip()
                if hobbies is not None:
                    hobbies = hobbies.strip()
                out_f.write(f'{users}: {hobbies}\n')


if __name__ == '__main__':
    program, user_file, hobbies_file, out_file = sys.argv
    users_and_hobbies(user_file, hobbies_file, out_file)
