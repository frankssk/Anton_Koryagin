def val_checker(valid):
    def wrapper(func):
        def validator(*args):
            if valid(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'wrong val: {args}')

        return validator

    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    z = x ** 3
    return z


print(calc_cube(-3))
