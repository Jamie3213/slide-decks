---
marp: true
---

# **Modern Python** 🐍

## Like Regular Python, But Better

---
## **What's wrong with how I write Python now?**

Nothing...necessarily 👀

---

## **New isn't always better**

* Just because I like it doesn't mean you have to
* Take what you like, and leave what you don't

___

## **Type hints**

<p style="font-size: 0.7em">(this is my favourite)</p>
</br>

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

The two biggest benefits of type hints are that they help us to:

* Document our code better, being explicit about the kinds of values we pass around
* Catch errors early (we'll see this more later)

---

## **But isn't Python dynamically typed?** 🤔

Type hints are **aesthetic**, they don't actually enforce anything in our code.

</br></br></br></br>
<p style="font-size: 0.8em">(we'll see later how we can get closer to something that looks like static typing 😍)</p>

---

* Show how to type hint functions with `Callable`
* Show how (and why) to define type aliases
* Show how typed generics work
* Talk about Mypy
