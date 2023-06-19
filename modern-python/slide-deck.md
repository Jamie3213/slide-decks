---
marp: true
---

# **Modern Python** 🐍

## Like Regular Python, But Better

---
## **What's wrong with how I write Python now?**

Nothing (necessarily)

---

## **New isn't always better**

* Just because I like it doesn't mean you have to
* Take what you like, and leave what you don't

___

## ✨ **Type hints** ✨

From this:

```python
def shout(word):
    print(f"{str.upper(word)}!")
```

To this:

```python
def shout(word: str) -> None:
    print(f"{str.upper(word)}!")
```

---

>Type hints help us **document our code more easily** and **catch errors early**.

---

## **But isn't Python dynamically typed?** 🤔

⚠️ Type hints are **aesthetic**, they don't actually enforce anything in our code. ⚠️

<br/>

![width:750px](./assets/type_hints_are_aesthetic.gif)

---

## **Type aliases**

```python
Point = tuple[float, float]

def scale(point: Point, factor: float) -> Point:
    return (factor * point[0], factor * point[1])


UserId = str

def delete_users(users: list[UserId]) -> None:
    for user in users:
        # Some logic here
```

---

## **Built-ins vs. `from typing import ...`**

```python
from typing Dict, List, Tuple

foo = List[int]
bar = list[int]

baz = Tuple[float, float]
qux = tuple[float, float]

spam = Dict[str, str]
ham = dict[str, str]
```

Built-ins are preferred (e.g., `list`, `dict`).

___

## **We can type-hint functions too**

```python
from typing import Any, Callable, Sequence

def apply(func: Callable[[Any], Any], values: Sequence[Any]) -> list[Any]:
    return [func(value) for value in values]

values = (1, 2, 3)
double = lambda x: 2 * x
applied_values = apply(double, values) # [2, 4, 6]
```

---

## **Avoid `Any` wherever you can**

* When we use `Any`, we're basically adding a type hint for the sake of it
* Objects annotated with `Any` **do not** get type checked

```python
from typing import Callable, Sequence

def apply(func: Callable, values: Sequence) -> list:
    return [func(value) for value in values]
```

---

## **Typed generics**

```python
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def apply(func: Callable[[T], U], values: Sequence[T]) -> list[U]:
    return [func(value) for value in values] 
```

---

## **What exactly is a `Sequence`?**

* Originates in `collections.abc`

* An interface that defines `__getitem__` and `__len__` abstract methods

* Classes like `list`, `tuple` and `str` are *"virtual subclasses"* of `Sequence`

```python
from typing import Sequence

issubclass(list, Sequence) # True
issubclass(tuple, Sequence) # True
issubclass(str, Sequence) # True
```

---

## **General in → specific out**

> If functions or methods only need their inputs to have generic behaviours (e.g., the ability to be sequenced or iterated over), then consider using ABCs in type annotations to maintain flexibility.

<br/>

ABCs like `Sequence`, `Mapping`, `Iterable`, `Iterator` etc. are all just interfaces with certain abstract methods that we need to override (usually dunder methods).

---

## **What if I want to subtype *my own* classes?**

```python
from typing import Generic, TypeVar


T = TypeVar("T")

class MagicList(Generic[T]):
    def __init__(self, *args: T) -> None:
        ...


magic_list: MagicList[int] = MagicList(1, 2, 3)
```

---

## **Nominal vs. structural subtyping**

---

```python
from abc import ABC


class MyClass(ABC):

    @abtsractmethod
    def my_method() -> None:
        """A method that does something"""

    @abstractmethod
    def my_other_method() -> None:
        """A method that does something else"""
```

---

* How does Any work
* Protocols vs abc.ABC
* Mypy and linters (show things like config to enforce no use of `Any`)
* Structural pattern matching
* Pre-commit

---

## **References**

* [`collections.abc` documentation](https://docs.python.org/3/library/collections.abc.html)
* [`Sequence` source code](https://github.com/python/cpython/blob/8bb16f665691b2869e107e180208d28b292bf3bd/Lib/_collections_abc.py#L973-L1039)