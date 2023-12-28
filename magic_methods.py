"""

Magic methods in Python, also known as dunder methods (from "double underscores"), are special methods with fixed names
that start and end with double underscores (`__`). They are a part of Python's object-oriented programming paradigm and
are used to provide an interface for integrating your objects with built-in Python operations or standard library
functions.

These methods allow your objects to emulate some built-in behavior of Python and hence, they are 'magical' in a way that
they are automatically triggered by the Python interpreter in certain circumstances. Here are some commonly used magic
methods:

1. **`__init__(self, [...])`**: The constructor method for a class. It's called when an object is created and
initializes the object's attributes.

2. **`__del__(self)`**: The destructor method. Called when an object is about to be destroyed.

3. **`__str__(self)`**: Called by the `str()` built-in function and by the `print` statement to compute the “informal”
 or nicely printable string representation of an object.

4. **`__repr__(self)`**: Called by the `repr()` built-in function and in many other contexts where a string
representation of the object is needed for debugging.

5. **`__len__(self)`**: Called to implement the built-in function `len()` for the object.

6. **`__getitem__(self, key)`**: Called to implement evaluation of `self[key]`.

7. **`__setitem__(self, key, value)`**: Called to implement assignment to `self[key]`.

8. **`__delitem__(self, key)`**: Called to implement deletion of `self[key]`.

9. **Arithmetic Magic Methods**:
   - **`__add__(self, other)`**: Implements addition.
   - **`__sub__(self, other)`**: Implements subtraction.
   - **`__mul__(self, other)`**: Implements multiplication.
   - And so on for other arithmetic operators.

10. **Comparison Magic Methods**:
    - **`__eq__(self, other)`**: Implements equality (`==`).
    - **`__ne__(self, other)`**: Implements inequality (`!=`).
    - **`__lt__(self, other)`**: Implements less than (`<`).
    - **`__gt__(self, other)`**: Implements greater than (`>`).
    - And so on for other comparison operators.

11. **`__call__(self, [...])`**: Allows the instance of a class to be called as a function.

12. **`__enter__(self)`/`__exit__(self, exc_type, exc_value, traceback)`**: Implements object context management. Used
 in with statements.

Magic methods provide a very powerful mechanism for extending and customizing the Python language in an elegant and
Pythonic way. They are fundamental to many of the succinct and expressive features of Python.

"""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            raise ValueError("Can only add another ComplexNumber")


# Creating two ComplexNumber objects
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 7)

# Using the overridden __str__ method
print("c1:", c1)  # Outputs: c1: 2 + 3i
print("c2:", c2)  # Outputs: c2: 1 + 7i

# Using the overridden __add__ method
c3 = c1 + c2
print("c1 + c2:", c3)  # Outputs: c1 + c2: 3 + 10i


# 1. **`__init__(self, [...])`**:
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 2. ** `__del__(self)` **:

class Logger:
    def __del__(self):
        print("Logger instance is being destroyed")


# 3. ** `__str__(self)` **:


class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


# 4. ** `__repr__(self)` **:


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# 5. ** `__len__(self)` **:


class Inventory:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)


# 6. ** `__getitem__(self, key)` **:


class Container:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]


# 7. ** `__setitem__(self, key, value)` **:


class Settings:
    def __init__(self):
        self._settings = {}

    def __setitem__(self, key, value):
        self._settings[key] = value


# 8. ** `__delitem__(self, key)` **:


class Basket:
    def __init__(self):
        self.items = {}

    def __delitem__(self, key):
        del self.items[key]


# 9. ** Arithmetic
# Magic
# Methods **:
# - ** `__add__(self, other)` **:


class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


# 10. ** Comparison
# Magic
# Methods **:
# - ** `__eq__(self, other)` **:


class Student:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


# 11. ** `__call__(self, [...])` **:


class Printer:
    def __call__(self, message):
        print(f"Printing {message}")


# 12. ** `__enter__(self)` / `__exit__(self, exc_type, exc_value, traceback)` **:


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
