from bisect import bisect, bisect_left
from collections.abc import Sequence
from itertools import chain
from typing import Any


class SortedSet(Sequence):
    def __init__(self, items=None) -> None:
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self) -> str:
        return f"SortedSet({repr(self._items) if self._items else ''})"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, SortedSet):
            return NotImplemented
        return self._items == __o._items

    def __ne__(self, __o: object) -> bool:
        if not isinstance(__o, SortedSet):
            return NotImplemented
        return self._items == __o._items

    def index(self, item: Any) -> int:
        index = bisect_left(self._items, item)

        if (index != len(self._items)) and (self._items[index] == item):
            return index

        raise ValueError(f'{repr(item)} not found')

    def count(self, item: Any) -> int:
        return int(item in self)

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    