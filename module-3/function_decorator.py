def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def north_city():
    return 'Noida¢'


def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(f'Args must be positive {index}')

            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size
