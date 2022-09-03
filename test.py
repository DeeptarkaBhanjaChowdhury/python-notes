class Test:

    @classmethod
    def create_with_number(cls, title, *args, **kwargs):
        return cls(title, *args, **kwargs)

    def __init__(self, title) -> None:
        self.title = title


test = Test.create_with_number('King', number=2)

print(test.number)
