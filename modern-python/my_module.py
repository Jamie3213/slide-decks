# from abc import ABC, abstractmethod

# class Sizeable(ABC):

#     @abstractmethod
#     def size(self) -> int:
#         ...

# def is_empty(container: Sizeable) -> bool:
#     return container.size() == 0


# class Trolley(Sizeable):
#     def __init__(self, items: list[str]) -> None:
#         self.items = items

#     def size(self) -> int:
#         return len(self.items)


# trolley = Trolley(["Bread", "Milk", "Eggs"])
# print(is_empty(trolley)) # False


# from typing import Sequence, TypeVar


# T = TypeVar("T")

# def first(values: Sequence[T]) -> T | None:
#     return values[0] if len(values) != 0 else None


# values = "Jamie"
# print(first(values))


# from typing import Protocol


# class Sizeable(Protocol):
#     def size(self) -> int:
#         ...


# def is_empty(container: Sizeable) -> bool:
#     return container.size() == 0


# class Trolley:
#     def __init__(self, items: list[str]) -> None:
#         self.items = items

#     def size(self) -> int:
#         return len(self.items)


# trolley = Trolley(["Bread", "Milk", "Eggs"])
# print(is_empty(trolley)) # False
# my_list = [1, 2, 3]
# print(is_empty(my_list))


from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    occupation: str


person = Person(
    name=100,
    age="Jamie",
    occupation={"name": "Jamie"},
)

print(person.name)
print(person.age)
print(person.occupation)

from dataclasses import asdict

print(asdict(person))

from pydantic.dataclasses import dataclass

@dataclass
class ValidatedClass:
    string: str
    integer: int


validated_class = ValidatedClass(string=100, integer="100")
