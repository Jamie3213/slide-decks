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

## **Typed generics**

```python
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def apply(func: Callable[[T], U], values: Sequence[T]) -> list[U]:
    return [func(value) for value in values]
```

---

## **General in → specific out**

Consider being more general in what your functions and methods accept but more specific in what they return:

* `list[str]` vs. `Sequence[str]`
* `dict[str, int]` vs. `Mapping[str, int]`

---

* Typed generics
* Structual vs. nominal sub-typing
* Protocols vs abc.ABC
* Talk about Mypy and linters
* How does Any work
