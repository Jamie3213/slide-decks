---
marp: true
---

# **Unit and Integration Testing**

## Who cares?

---

## **Why do we test?**

* Catch issues early
* Support refactoring
* Document our code
* Deliver better code, faster

---

## **When _should_ we test?**

* Before we implement a piece of functionality (**Test Driven Development**):

    * **<span style="color:red;">RED</span>** - write a test, make sure it fails
    *  **<span style="color:green;">GREEN</span>** - write the simplest piece of code to make the test pass
    *  **<span style="color:grey;">REFACTOR</span>** - make changes under the comfort of a passing test

* Writing tests first means we need to be able to define the problem (it stops us writing rambling code without clear intention)
* We inherently write code that's more easily testable

---

## **Unit vs. integration tests?**

Unit tests:

* Test individual _units_ of functionality
* Are isolated, with no dependency on external systems
* Specific, with only one reason to fail
* Fast, giving us quick feedback

Integration tests:

* Test how multiple units of funtionality interact
* Often involve interaction with external systems
* Often more complex and slower to run

---

## **Which do we use when?**

<br>
<br>

![](./assets/data_pipeline.png)

---

* Focus the bulk of testing on the transformation stage using unit tests
* Use integration tests to:

  * Test interactions between units of transformation logic where necessary
  * Test interactions with external systems, e.g., does our table create properly, is our data correctly merged into a target table

* Try to push out the boundaries where we interact with external systems so we can isolate and predictably test as much of our code as possible