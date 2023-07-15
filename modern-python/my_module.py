from typing import Callable, Sequence, TypeVar


T = TypeVar("T")
U = TypeVar("U")


def apply(func: Callable[[T], U], values: Sequence[T]) -> list[U]:
    return [func(value) for value in values]


# Valid to a type checker ✅
numbers: tuple[int, int, int] = (1, 2, 3)
double: Callable[[int], int] = lambda x: x * 2
doubled = apply(double, numbers)

# Invalid to a type checker ❌
words: list[str] = ["one", "two", "three"]
square: Callable[[int], int] = lambda x: x ** 2
squared = apply(square, words)
