---
marp: true
---

<!--
* What we're going to talk about
* Talk is based on the blog "Pragmatic Functional Programming in Python"
-->

# **Monads in Python**

## How They Work & Why You Shouldn't Use Them

---

## **...who cares?** 🫠

* Functional programming without an understanding of Monads is hard
* Pure functional languages like Haskell use Monads everywhere
* Lots of FP resources are framed in the context of Haskell

---

## **What makes code functional?**

> Functional programming is about building functionality through the composition of pure functions.

---

## **Intermediary variables are for losers**

We could do this:

```python
f_result = f(x)
g_result = g(f_result)
h_result = h(g_result)
```

...or we could cut out the middle man:

```python
h_result = h(g(f(x)))
```

(If only there was a prettier way to do this 🥺)

---

## **What makes a function "pure"?**

* Referential transparency
* Freedom from side-effects

---

### ✨ Pure ✨

```python
def add(a: int, b: int) -> int:
    return a + b
```

✅ Referentially transparent
✅ Free from side-effects

</br>

### 🤮 Impure 🤮

```python
def add(a: int, b: int) -> int:
    print(f"Adding {a} and {b}.")
    return a + b
```

❌ Referentially transparent
❌ Free from side-effects

---

### **Some things a pure function can't do** 🙃

* Log to console, file, stream etc.
* Read/write files
* Read from/write to a database
* Get user input
* Generate random numbers
* Call a REST API
* Raise exceptions

---

## **...so how do we get anything done?** 😒

> Functors, Applicatives and Monads help us handle side-effects and compose functions together

---

## **What's a Functor?**

A way to wrap a value in order to **encode behaviour**.

</br>

Sometimes spoken about as:

* "A box we put values into"
* "A value wrapped in a computational context"

---

### **Exception handling with `Either`**

<!-- markdownlint-disable MD033 -->
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

</br>

![width:600px center](assets/either.svg)

---

When `b == 0`, a `ZeroDivisionError` is raised.

```python
def divide(a: float, b: float) -> float:
    return a / b
```

---

Even when `b == 0`, no exception is raised and we consistently return an instance of `Either`.

```python
from pymonad.either import Either, Left, Right


def divide(a: float, b: float) -> Either[ZeroDivisionError, float]:
    if b == 0:
        return Left(ZeroDivisionError)
    else:
        return Right(a / b)
```

---

## **Pure functions are honest** 😇

 > The type signature of a pure function tells us about the good days *and* the bad days

---

## **I have this dream where I'm trapped in a Functor and I can't get out**

How do we get values out of `Either`?

```python
success = divide(1.0, 2.0)
failure = divide(1.0, 0.0)

# 0.5
success.either(
    lambda left: print(left),
    lambda right: print(right)
)

# ZeroDivisionError
failure.either(
    lambda left: print(left),
    lambda right: print(right)
)
```

---

## **You can't fit a square peg in a round hole**

How do we pass an `Either` into a normal function?

```python
add_one = lambda a: a + 1
zero_point_five = divide(1.0, 2.0)

# TypeError: unsupported operand type(s) for +: 'Either' and 'int'
add_one(zero_point_five)

```

---

## **Compose like Beethoven with `fmap`**

We can use a Functor's `fmap` method to compose functions.

```python
def fmap(self: "Functor[T]", function: Callable[[T], U]) -> "Functor[U]": ...
```

<!-- markdownlint-disable MD033 -->
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

</br>

![width:800px center](assets/fmap.svg)

---

## **Round peg, round hole**

Instead of passing an `Either` straight into `add_one`, we just use its `map` method.

```python
result = divide(1.0, 2.0).map(add_one)

# 1.5
result.either(
    lambda left: print(left),
    lambda right: print(right)
)
```

Annoyingly, PyMonad renamed `fmap` to `map` in its latest release 👎

---

## **Compose to your heart's content**

```python
add_ten = lambda a: a + 10
multiply_by_two = lambda a: a * 2
cube = lambda a: a ** 3
convert_to_int = lambda a: int(a)
format_as_string = lambda a: f"{a:,}"

result = (
    divide(4.0, 2.0)
    .then(add_ten)
    .then(multiply_by_two)
    .then(cube)
    .then(convert_to_int)
    .then(format_as_string)
)

# 13,824
result.either(
    lambda left: print(left),
    lambda right: print(right)
)
```

---

## **There isn't much more to a Functor**

Functors are just a means to:

* Handle side-effects to maintain functional purity
* Compose functions

---

## **All this talk of curry is making me hungry**

> Currying converts a function of `n` parameters into `n` functions, each with a single parameter.

</br>

```python
from pymonad.tools import curry

@curry(2)
def add_n(n: int, a: int) -> int:
    return a + n

add_one = add_n(1)
add_two = add_n(2)

# 2, 3
print(add_one(1), add_two(1), sep=", ")
```

---

## **What happens if we want to use a curried function directly in a composition chain?**

```python
result = (
    divide(1.0, 2.0)
    .map(add_n)
    . # Erm...what now?
)
```

* `map(add_n)` returns a function wrapped in a Functor
* We can't use another call to `map` to pass a value into the function because `map` doesn't know what to do with a function wrapped in a Functor


---

## **What's an Applicative?**

Applicatives are like Functors but they define a different method, this time called `amap`

```python
def amap(self: "Applicative[Callable[[T], U]]", value: "Applicative[T]") -> "Applicative[U]": ...
```

<!-- markdownlint-disable MD033 -->
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

</br>

![width:800px center](assets/amap.svg)

---

## **How is `amap` useful to us?**

> `Either` is a Functor because it defines an `fmap` method, but it's also an Applicative because it also defines an `amap` method.

</br>

```python
result = (
    divide(1.0, 2.0) # Right(0.5)
    .map(add_n) # Right(<add_n, n=0.5>)
    .amap(Right(0.5)) # Right(1.0)
)

# 1.0
result.either(
    lambda left: print(left),
    lambda right: print(right)
)
```

---

## **It turns out that Applicatives aren't too bad either**

Applicatives combined with currying allow to:

* Use multi-parameter functions in composition
* Pass values from outside the chain into functions
