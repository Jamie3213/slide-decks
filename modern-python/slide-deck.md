---
marp: true
paginate: true
---

# **Modern Python** 🐍

## Like regular Python, but better (IMO)

<!-- Thanks everyone for joining the second Python Community talk today. -->
<!-- I'm Jamie, I'm a data engineer in the Data & AI practice -->
<!-- I'm going to talk today about what I'm loosely calling "Modern Python" and hopefully you'll see what I mean by that as I go on. -->

---

## **What's wrong with how I write Python now?**

Nothing (necessarily)

<!-- Before we get into anything, let's answer a first question: what's wrong with the Python you're writing now? -->
<!-- I don't know what kind of Python you write but I'd argue there's probably nothing wrong with it. -->

---

## **New isn't always better**

* Just because I like it doesn't mean you have to
* Take what you like, and leave what you don't

<!-- One of the important things to say at the top is that I'm going to talk about some newer features of Python, but
just because a feature is new doesn't mean it's better. -->
<!-- On top of that, just because I like a feature doesn't necessarily mean you will as well. -->
<!-- There's nothing cut and dry here, it's my opinion that writing in the style I'll show you is better, but that
doesn't make it true. -->
<!-- My advice would be, if there's anything I talk about today that you like, then adopt it in your code. -->
<!-- If there are things I talk about that you don't like, then don't adopt those things. -->
<!-- With that said, let's start with what is, hands-down, my favourite Python feature... -->

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

<!-- So what do type hints do? -->
<!-- I've got two blocks of code here which each define the same function "shout". -->
<!-- "shout" takes in a string and then uppercases that string and prints it to the console. -->
<!-- In the first block, I've got shout written with a traditional Python syntax -->
<!-- In the second block, I've got shout written using "type annotations" or "type hints" -->
<!-- Hopefully it's clear that all type hints do here is that they provide an explicit defintiion of expected type of the functions inputs along with the expected type of its output. -->
<!-- So here I specify that "word" is of type string, and I use the built-in Python string class to do that, and since all I do is print to the console, my function implicitly returns None, so then I use this arrow syntax and give a type hint to say that my function returns None. -->
<!-- And in its simplest form, that's what type annotations look like in Python -->
---

## **Why would I want to use type hints?**

>Type hints help us **document our code more easily** and **catch errors early**.

<!-- So why are these type annotations something that you'd be ineterested in using? -->
<!-- To me there are two main benefits to using type hints. -->
<!-- The first I think is already evident in that simple example which is that using type hints lets us document our code more easily. By defining the inputs and outputs of our functions explcitly we make it much easier for the people reading and using our code to understand it. -->
<!-- The second is that using type hints lets us catch errors earlier than we otherwise would, and we'll talk in some more depth about that a bit later. -->

---

## **But isn't Python dynamically typed?** 🤔

⚠️ Type hints are **aesthetic**, they don't actually enforce anything in our code. ⚠️

```python
def say_hello(name: str) -> None:
    print(f"Hello, {name}!")


# Prints 'Hello, 100!'
say_hello(100)
```

<!-- One thing you might already be thinking is, wait, isn't Python a dynamically typed language? -->
<!-- Yes, Python is and presumably will always be a dynamically typed language. -->
<!-- One of the most important things to emphasise at this point is that type hints are purely aesthetic - they have absolutely no impact on the running of your code. -->
<!-- Python couldn't care less what type annotations you use, as long as at runtime it can run your code without errors -->
<!-- So as an example here I've got this "say_hello" function which just prints an interpolated string to the console using the name we pass in. -->
<!-- If we call that function with 100, an integer, as the argument, Python will still run that function just fine because it knows how to coerce an integer to a string. -->
<!-- Again, the interpreter doesn't respect or know anything about type annotations we use. -->

---

## **Sub-typing**

Lots of classes in Python have a natural concept of a *sub-type*, e.g., a collection of type A contains elements of type B.

```python
list[str]
tuple[int, int]
tuple[int, ...]
dict[str, str | None]  # dict[str, Optional[str]]
dict[str, int | float]  # dict[str, Union[int, float]]
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

<!-- Type aliases are a nice way to try and convey more meaning from a type hint. -->
<!-- So here I've defined a "Point" and Point is just a type alias for a tuple of two floats. -->
<!-- Even though Point isn't a class, I can now use it like one in my type hints. -->
<!-- I've got another example here where I alias a string as a UserId, and then I use that in my function and sub-type list, so my function takes a list of user IDs and then does some processing of them. -->
<!-- I don't think type hints are ground-breaking at all but they can be useful occasionally like I said as a way to impart a bit more meaning or context to your type hints. -->

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

---

## **We can type-hint functions too**

```python
from typing import Any, Callable, Sequence


# Syntax: Callable[[InputType, InputType, ...], ReturnType]

def apply(func: Callable[[Any], Any], values: Sequence[Any]) -> list[Any]:
    return [func(value) for value in values]

values = (1, 2, 3)
double = lambda x: 2 * x
applied_values = apply(double, values)  # [2, 4, 6]
```
<!-- We've seen how to type hint simple variables or collections like lists or dictionaries, but we can also type hint more complex things like functions. -->
<!-- When we type hint a function we use a Callable that we import from the typing module. -->
<!-- We sub-type Callable and provide a list of input types and then the return type for the function. -->

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

## **Typed generics**

```python
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
```

---

## **What exactly is a `Sequence`?**

* Originates in `collections.abc`
* `collections.abc` defines useful interfaces for general Python data collections
* The `Sequence` interface that defines `__getitem__` and `__len__` abstract methods
* Classes like `list`, `tuple` and `str` are *"virtual subclasses"* of `Sequence`

```python
from typing import Sequence


issubclass(list, Sequence)  # True
issubclass(tuple, Sequence)  # True
issubclass(str, Sequence)  # True
```

---

## **General in → specific out**

> If functions or methods only need their inputs to have generic behaviours (e.g., the ability to be sequenced or iterated over), then consider using ABCs in type annotations to maintain flexibility.

<br/>

ABCs like `Sequence`, `Mapping`, `Iterable` and `Iterator` are all just interfaces with abstract methods for us to override - usually dunder methods like `__get__` or `__next__`.

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

## **Black is *opinionated***

Actually, Black is *very* opinionated:

* Sometimes you won't like how if formats your code
* Sometimes you'll like how it formats your code and another person in your team won't

    ```python
    # True ✅
    no_one_fully_happy + consistent == everyone_happy
    ```

    (but if you're *really* unhappy, it's configurable)

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

## **When you run Isort it...**

* Splits imports into separate stdlib and non-stdlib import blocks
* Auto-sorts import blocks alphabetically
* Auto-sorts `import ...` and `from ... import ...`
* Even has native compability with Black:

    ```bash
    $ isort my_module.py --profile black
    Fixing my_module.py
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

## **References**

* [PEP-484 - Type Hints](https://peps.python.org/pep-0484/)
* [`collections.abc` docs](https://docs.python.org/3/library/collections.abc.html)
* [`Sequence` source code](https://github.com/python/cpython/blob/8bb16f665691b2869e107e180208d28b292bf3bd/Lib/_collections_abc.py#L973-L1039)
* [Mypy docs](https://mypy.readthedocs.io/en/stable/)
* [Mypy configuration docs](https://mypy.readthedocs.io/en/stable/config_file.html)
* [Pre-commit docs](https://pre-commit.com)
