from unittest import result


class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def _get_next_serial_cls(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    def __init__(self, owner_code, contents) -> None:
        self.owner_code = owner_code
        self.contents = contents
        # self.serial = ShippingContainer._get_next_serial()
        ''' use self for polymorphic usage'''
        self.serial = ShippingContainer._get_next_serial_cls()

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self ._p = value
