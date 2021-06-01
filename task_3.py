def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        result = func(*args)
        return result

    return wrapper


@type_logger
def calc_in_extent(x, y):
    z = x ** y
    return z


print(calc_in_extent(3, 3))
