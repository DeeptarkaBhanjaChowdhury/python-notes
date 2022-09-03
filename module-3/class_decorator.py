

class CallCount:
    def __init__(self, f) -> None:
        self.f = f
        self.count = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print(f'Hello, {name}')


class Trace:
    def __init__(self) -> None:
        self.enabled = True

    def __call__(self, f, *args: Any, **kwds: Any) -> Any:
        def wrap(*args, **kawrgs):

            if self.enabled:
                print(f'Calling {f}')

        wrap.__name__ = f.__name__
        wrap.__doc__ = f.__doc__
        return wrap


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
