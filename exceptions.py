import math


class TriangleError(Exception):
    def __init__(self, text, sides, *args: object) -> None:
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    def __str__(self) -> str:
        return f'{self.args[0]} for sides {self._sides}'

    def __repr__(self) -> str:
        return f'TriangleError({self.args[0], self._sides})'


def triangle_area(a, b, c):
    sides = sorted((a, b, c))

    if sides[2] > sides[0] + sides[1]:
        raise TriangleError('Illegal triangle')

    p = (a + b + c) / 2
    a = math.sqrt(p * (p-a) * (p-b) * (p-c))
    return a
