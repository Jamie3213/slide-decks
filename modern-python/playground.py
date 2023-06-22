from abc import ABC, abstractmethod

class Sizeable(ABC):

    @abstractmethod
    def size(self) -> int:
        ...

def is_empty(container: Sizeable) -> bool:
    return container.size() == 0


class Trolley(Sizeable):
    def __init__(self, items: list[str]) -> None:
        self.items = items

    def size(self) -> int:
        return len(self.items)


trolley = Trolley(["Bread", "Milk", "Eggs"])
print(is_empty(trolley)) # False


from typing import Sequence, TypeVar


T = TypeVar("T")

def first(values: Sequence[T]) -> T | None:
    return values[0] if len(values) != 0 else None


values = "Jamie"
print(first(values))
