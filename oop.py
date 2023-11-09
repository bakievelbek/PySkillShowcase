"""

Object-Oriented Programming (OOP) is a paradigm that uses "objects" to design applications and computer programs.
It utilizes several principles such as encapsulation, inheritance, and polymorphism.

"""

# Abstraction in object-oriented programming is the concept of hiding the complex reality while exposing only the
# necessary parts. It's a way of creating a simple model of a more complex underlying structure that represents all
# the same functionalities but in a simplified manner.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Subclass that implements the abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


"""
In this example, Shape is an abstract class with abstract methods area and perimeter. 
The Rectangle class implements these methods. If you try to instantiate Shape, 
Python will raise an error because it's not allowed to create objects from abstract classes.

"""

# Encapsulation is one of the fundamental principles of object-oriented programming.
# It's the bundling of data with the methods that operate on that data, or the restriction of direct access to some
# of an object's components. Encapsulation means that the internal representation of an object is generally hidden
# from view outside of the object's definition.

"""
In Python, encapsulation is not enforced by the language, but it follows a convention of prefixing the name of the
 variable with an underscore (_) to indicate to the programmer that it is intended for internal use only. This is 
 known as a "weak" form of encapsulation because it is based on convention rather than language enforcement. Python 
 also has name mangling for attributes prefixed with double underscores which makes it harder (but not impossible) 
 to access from outside the class.

"""


class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # intended as a protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._update_ledger(amount)

    def _update_ledger(self, amount):  # intended as a protected method
        print(f"Ledger updated with deposited amount: {amount}")


# Outside access
account = BankAccount(1000)
account.deposit(500)
print(account._balance)  # Not recommended, but possible due to Python's nature

# In the above Python example, the _balance variable and _update_ledger() method are meant to be protected members:
# they can be accessed but should not be according to the convention.

'''
Polymorphism is an object-oriented programming concept that refers to the ability of a variable, function, or object
to take on multiple forms. The word "polymorphism" comes from Greek, meaning "many shapes." In programming, it allows
objects to be treated as instances of their parent class rather than their actual class. The two most common types of
polymorphism are:

    Compile-time polymorphism (also known as static polymorphism): This type of polymorphism is achieved by function
    overloading or operator overloading. However, not all languages support these features. For example, Python does
    not support method overloading by default, but you can achieve a similar effect in different ways, such as with
    default arguments or variable-length argument lists.

    Run-time polymorphism (also known as dynamic polymorphism): This type of polymorphism is achieved by method
    overriding, which is when a subclass provides a specific implementation of a method that is already defined 
    in its parent class.
'''


class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# Polymorphic function
def animal_sound(animal: Animal):
    print(animal.speak())


# List of animal objects
animals = [Animal(), Dog(), Cat()]

# Looping through animals
for animal in animals:
    animal_sound(animal)


# This code will output:
# Some sound
# Woof
# Meow


# Inheritance is a fundamental principle of object-oriented programming that allows a class to inherit properties
# and behavior (methods) from another class. The class that inherits is called the subclass (or derived class),
# and the class being inherited from is called the superclass (or base class).


# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print("The engine is starting.")


# Subclass
class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model)  # Call the superclass constructor
        self.horsepower = horsepower

    def start_engine(self):
        super().start_engine()  # Call the method from the superclass
        print("Vroom! The car's engine is running.")


# Use the Car subclass
my_car = Car("Toyota", "Corolla", 132)
my_car.start_engine()

"""

In this Python example, the Car class inherits from the Vehicle class. The Car class has all properties and methods of
the Vehicle, but it also adds its own horsepower property and extends the start_engine method.

"""
