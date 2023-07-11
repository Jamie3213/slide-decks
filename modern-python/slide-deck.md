---
marp: true
paginate: true
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

---

## **Structural pattern matching**

* Python's (less useful), version of Scala pattern matching
* Similar to `if` statements
* Used for checking the _structure_ of an object, not just its value

---

We can avoid code like `if isinstance(animal, Dog)` using the `match` syntax:

```python
match animal:
    case Dog():
        print("woof!")
    case Cat():
        print("meow!")
    case Bird():
        print("tweet!")
    case _:
        print("Wait, there are more than three animals?!")
```

---

We can easily destructure objects using the `match` syntax:

```python
match point:
    case (0, _):
        print("Has no x-component")
    case (_, 0):
        print("Has no y-component")
    case (x, y):
        print(f"x={x}, y={y}")
    case _:
        print("Not a point")
```

---

We can even hone in on specific parts of an object and ignore the rest:

```python
match order:
    case {"order_type": "order_placed", **rest}:
        print(f"Order placed")
    case {"order_type": "order_cancelled", **rest}:
        print("Order cancelled")
    case _:
        print("Something else")
```

---

## **When would I acually use this?**

* Most useful when matching some aspect of the overall object structure
* If matching against literals, it's usually easier to just use the more familiar if/else

---

## **Consistently format your code with Black**

* Poor formatting makes reading code and spotting mistakes hard
* We can use a code formatter like **Black** to enforce consistent formatting in our projects
* Installed with `pip`, `poetry`, `conda` etc.
* IDE plug-ins available

---

## **How does it work?**

```bash
$ black my_module.py
reformatted my_module.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

---

```python
# In
my_long_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "ninth", "tenth"]

# Out
my_long_list = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eigth",
    "ninth",
    "tenth",
]
```

---

```python
# In
result = Client().do_this()\
    .then_do_this()\
    .then_this()\
    .and_finally_this()

# Out
result = (
    Client().do_this()
    .then_do_this()
    .then_this()
    .and_finally_this()
)
```

---

## **Black is _opinionated_**

Actually, Black is _very_ opinionated:

* Sometimes you won't like how if formats your code
* Sometimes you'll like how it formats your code and another person in your team won't

```python
# True ✅
no_one_fully_happy + consistent == everyone_happy
```

(but if you're _really_ unhappy, it's configurable)

---

## **Stop manually sorting your imports**

* Sort your imports with Isort
* Installed like Black - `pip`, `poetry`, `conda` etc.

```bash
$ isort modern-python/my_module.py
Fixing my_module.py
```

---

```python
# In
from datetime import timezone, datetime, timedelta
import asyncio
from airflow.models.baseoperator import BaseOperator
import functools


# Out
import asyncio
import functools
from datetime import datetime, timedelta, timezone

from airflow.models.baseoperator import BaseOperator
```

---

* Splits imports into separate stdlib and non-stdlib import blocks
* Auto-sorts import blocks alphabetically
* Auto-sorts `import ...` and `from ... import ...`
* Even has native compability with Black:

    ```bash
    $ isort my_module.py --profile black
    Fixing my_module.py
    ```

---

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

```python
def say_hello(name: str) -> None:
    print(f"Hello, {name}!")


# Prints 'Hello, 100!'
say_hello(100)
```

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

Built-ins are preferred, e.g., `list`, `dict`.

___

## **We can type-hint functions too**

```python
from typing import Any, Callable, Sequence


def apply(func: Callable[[Any], Any], values: Sequence[Any]) -> list[Any]:
    return [func(value) for value in values]

values = (1, 2, 3)
double = lambda x: 2 * x
applied_values = apply(double, values)  # [2, 4, 6]
```

---

## **Avoid `Any` wherever you can**

* When we use `Any`, we're basically adding a type hint for the sake of it
* Objects annotated with `Any` **do not** get type checked
* We can leave `Any` out and it will be inferred by a type checker

```python
from typing import Callable, Sequence


def apply(func: Callable, values: Sequence) -> list:
    return [func(value) for value in values]
```

---

## **What exactly is a `Sequence`?**

* Originates in `collections.abc`

* An interface that defines `__getitem__` and `__len__` abstract methods

* Classes like `list`, `tuple` and `str` are *"virtual subclasses"* of `Sequence`

```python
from typing import Sequence


issubclass(list, Sequence)  # True
issubclass(tuple, Sequence)  # True
issubclass(str, Sequence)  # True
```

---

## **Typed generics**

```python
from typing import Callable, Sequence, TypeVar


T = TypeVar("T")
U = TypeVar("U")


def apply(func: Callable[[T], U], values: Sequence[T]) -> list[U]:
    return [func(value) for value in values]


def first(values: Sequence[T]) -> T | None:
    return values[0] if len(values) != 0 else None
```

---

## **General in → specific out**

> If functions or methods only need their inputs to have generic behaviours (e.g., the ability to be sequenced or iterated over), then consider using ABCs in type annotations to maintain flexibility.

<br/>

ABCs like `Sequence`, `Mapping`, `Iterable` and `Iterator` are all just interfaces with abstract methods for us to override - usually dunder methods like `__get__` or `__next__`.

---

## **What if I want to subtype _my own_ classes?**

```python
from typing import Generic, TypeVar


T = TypeVar("T")

class MagicList(Generic[T]):
    def __init__(self, *args: T) -> None:
        ...


magic_list: MagicList[int] = MagicList(1, 2, 3)
```

---

## **Nominal vs. structural typing**

Nominal → compatibility determined from declared type - ***"is it?"***
Structural → compatibility determined from structure - ***"does it?"***

---

## **Interfaces - ABCs or Protocols?**

* Languages like Java make a distinction between *interfaces* and *abstract classes*
* In Python, we talk about interfaces and abstract classes interchangeably
* When we talk about an interface, we're really just thinking of a *blueprint*
* We can define an interface using either `abc.ABC` or `typing.Protocol`

---

## **Using `abc.ABC` fits a nominal typing style**

```python
from abc import ABC, abstractmethod


class Sizeable(ABC):

    @abstractmethod
    def size(self) -> int:
        ...
```

---

To use an ABC, we have to explicitly inherit from the parent class.

```python
def is_empty(container: Sizeable) -> bool:
    return container.size() == 0


class Trolley(Sizeable):
    def __init__(self, items: list[str]) -> None:
        self.items = items

    def size(self) -> int:
        return len(self.items)

    def add_item(item: str) -> None:
        self.items = [*self.items, item]


trolley = Trolley(["Bread", "Milk", "Eggs"])
print(is_empty(trolley))  # False

```

---

## **Using `typing.Protocol` fits a structrual style**

Protocols let us make use of static duck-typing and help us to define generic type bounds.

```python
from typing import Protocol


class Sizeable(Protocol):

    def size(self) -> int:
        ...
```

---

```python
def is_empty(container: Sizeable) -> bool:
    return container.size() == 0


class Trolley:  # No need to inherit from Sizeable
    def __init__(self, items: list[str]) -> None:
        self.items = items

    def size(self) -> int:
        return len(self.items)

    def add_item(item: str) -> None:
        self.items = [*self.items, item]


trolley = Trolley(["Bread", "Milk", "Eggs"])
print(is_empty(trolley))  # False
```

---

Python is already duck-typed, so couldn't we just have left out type annotations and still run the program as normal?

(Yes 😬)

---

## **Is it worth all the effort?**

* To really take advantages of type hints, we need to use a **static type checker**
* We incoporate type checkers into our workflow and flag when type checking fails
* We try to convert runtime errors into pre-runtime errors from the type checker

---

## **Mypy to the rescue** 🦸‍♀️

* Most popular static type checker for Python
* CLI support and IDE integration (e.g., VS Code, IntelliJ IDEs)
* Active contributors include Guido van Rossum
* Installed like any Python package (`pip`, `poetry`, `conda` etc.)

---

## **What does it do?**

```python
# my_module.py
from typing import Protocol


class Sizeable(Protocol):

    def size(self) -> int:
        ...


def is_empty(container: Sizeable) -> bool:
    return container.size() == 0


my_list = [1, 2, 3]
print(is_empty(my_list))
```

---

Without a type checker, we only find out about errors in our code when we run it:

```shell
$ python my_module.py
Traceback (most recent call last):
  File "my_module.py", line 16, in <module>
    print(is_empty(my_list))
          ^^^^^^^^^^^^^^^^^
  File "my_module.py", line 12, in is_empty
    return container.size() == 0
           ^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'size'
```

---

With a type checker like Mypy, we flag the type error before ever running the code:

```shell
$ mypy my_module.py
my_module.py:16: error: Argument 1 to "is_empty" has incompatible type "List[int]"; expected "Sizeable"
Found 1 error in 1 file (checked 1 source file)
```

---

## **What's the big deal?**

* We found an error in our code without actually running it
* We turned what _would've_ been a runtime error into a pre-runtime error
* Imagine an ML workflow failing after 10 hours because you mis-typed a method name
* With Mypy, we catch these errors early and avoid more pain further down the line

---

## **We can get real-time feedback in our IDE**

---

## **Mypy is configurable**

We can add a `mypy.ini` file to our project and configure aspects of type checking:

```text
[mypy]
disallow_any_expr = True
disallow_untyped_defs = True
```

We can even disable type checking on specific lines:

```python
something = ...  # type: ignore
```

---

## **Bring your CI pipeline closer to home with pre-commit**

* Pre-commit is a Python-based framework for managing Git hooks
* We can configure hooks to run everytime we commit (which should be often!)
* Pre-commit has a bank of pre-defined, easy-to-use hooks
* Hooks already exist for Black, Isort and Mypy!
* Easily installed with `pip`, `conda`, `brew` etc.

---

We configure our hooks with using a `.pre-commit-config.yaml` file:

```yaml
repos:
  -   repo: https://github.com/pre-commit/mirrors-mypy
      rev: v1.4.1
      hooks:
      -   id: mypy
          name: Run Mypy static type checking
  -   repo: https://github.com/psf/black
      rev: 23.7.0
      hooks:
      -   id: black
          name: Format Python code in Black style
  -   repo: https://github.com/PyCQA/isort
      rev: 5.12.0
      hooks:
      -   id: isort
          args: ["--profile", "black"]
          name: Sort module imports with Isort
```

---

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit

$ pre-commit run --all-files
Run Mypy static type checking............................................Failed
- hook id: mypy
- exit code: 1

modern-python/my_module.py:20: error: "list[int]" has no attribute "size"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

Format Python code in Black style........................................Failed
- hook id: black
- files were modified by this hook

reformatted modern-python/my_module.py

All done! ✨ 🍰 ✨
1 file reformatted.

Sort module imports with Isort...........................................Passed
```

---

```shell
# After fixing errors
$ git add --all
$ git commit -m "My great new feature"
Run Mypy static type checking............................................Passed
Format Python code in Black style........................................Passed
Sort module imports with Isort...........................................Passed

```

---

* Tons of existing hooks, including checks for:
  * Mixed line endings
  * Trailing whitespace
  * Validate terraform, run tflint etc.
  * Format YAML, JSON, TOML etc.
* Easy to define custom hooks, e.g., to run unit tests on commit
* Create a tighter feedback loop and bring your CI checks closer to you
* Support for other languages/frameworks like `node`, `dotnet`, `golang`, `rust`, `r`

---

## **Give your data structure with data classes**

* Avoid passing data around as naked Python objects
* Provide a schema without the need for verbose class syntax

---

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    occupation: str
    hobbies: list[str]

external_data = {
    "name": "Jamie",
    "age": 29,
    "occupation": "Data Engineer",
    "hobbies": ["Python", "Python", "More Python"]
}

jamie = Person(**external_data)
```

---

Without data classes, things don't look anywhere near as pretty 🤮

```python
class Person:
    def __init__(
        self,
        name: str,
        age: int,
        occupation: str,
        hobbies: list[str],
    ) -> None:
        self.name = name
        self.age = age
        self.occupation = occupation
        self.hobbies = hobbies
```

---

## **Data classes come with lots of nice features...**

* Data classes are much cleaner and more readable.
* We can define methods on data classes like we would with a normal class.
* We get boring methods like `__init__`, `__repr__`, `__eq__`, `__ne__` etc. for free.
* We can use `@datclass(frozen=True)` to make instances immutable.
* Functions like `dataclasses.asdict` can convert the data class back to a `dict`.

---

## **...but they're also deceptive**

```python
from dataclasses import dataclass


@dataclass
class UnvalidatedClass:
    string: str
    integer: int


data = {
    "string": 100,
    "integer: "100",
}

# Instantiates without issue ⚠️
unvalidated_class = UnvalidatedClass(**data)
```

---

## ⚠️ **PSA** ⚠️

* Data class inputs aren't validated for type.
* We can pass anything we want as the arguments to the class.
* We can use magic methods like `__post_init__` to validate inputs, but that's ugly!

---

## **Consider `pydantic` data classes**

* Like normal data classes on steroids
* Can validate inputs based on type

```python
from pydantic.dataclasses import dataclass


@dataclass
class ValidatedClass:
    string: str
    integer: int


# Throws the validation error:
#
# ValidationError: 1 validation error for ValidatedClass
# Input should be a valid string [type=string_type, input_value=100, input_type=int]
validated_class = ValidatedClass(string=100, integer="100")

```

---

## **As always, it's about tradeoffs**

* Richer functionality for data parsing and serialization with `pydantic`
* Yet another external dependency in a project
* Much less light-weight than `dataclasses.dataclass`

---

## **Key takeaways**

---

## **References**

* [PEP-636 - Structural Pattern Matching](https://peps.python.org/pep-0636/)
* [PEP-484 - Type Hints](https://peps.python.org/pep-0484/)
* [`collections.abc` docs](https://docs.python.org/3/library/collections.abc.html)
* [`Sequence` source code](https://github.com/python/cpython/blob/8bb16f665691b2869e107e180208d28b292bf3bd/Lib/_collections_abc.py#L973-L1039)
* [Mypy docs](https://mypy.readthedocs.io/en/stable/)
* [Mypy configuration docs](https://mypy.readthedocs.io/en/stable/config_file.html)
* [Pre-commit docs](https://pre-commit.com)
* [Python data class docs](https://docs.python.org/3/library/dataclasses.html)
* [Pydantic data class docs](https://docs.pydantic.dev/latest/)
