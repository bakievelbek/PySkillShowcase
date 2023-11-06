"""
In Python, a decorator is a design pattern that allows you to add new functionality to an existing object without
modifying its structure. Decorators are a very powerful and useful tool in Python since they allow for the modification
of functions or methods using other functions. They are usually called before the definition of a function you want
to decorate.

"""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# This will print:
# "Something is happening before the function is called."
# "Hello!"
# "Something is happening after the function is called."
say_hello()

"""
Common Python Decorators: property, classmethod, and staticmethod
"""


# property:
# The property decorator is used to create managed attributes in object-oriented programming.
# This decorator turns a method into a "getter" for a read-only attribute with the same name.
# In this example, name is a managed attribute. You access it like a normal attribute (person.name),
# but when accessed, the name method is automatically called to compute the value.


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        """I am the 'name' property."""
        return self._name

    def surname(self):
        return self._surname


# Comparison of simple function with a decorator function

person = Person(name='Elbek', surname='Bakiev')

"""

classmethod:
The classmethod decorator is used to define a method in a class that is bound to the class and not the instance of
the class. This means that the class is passed as the first argument instead of the instance (self).

The term "factory method" in object-oriented programming refers to a method that is used for creating objects, rather
 than by calling a constructor directly. This pattern is particularly useful when the process of constructing an object 
 is complex, or when it should be separate from the main class to allow for easier scalability and maintenance. 
 The classmethod decorator plays an important role in implementing factory methods in Python.

Here’s how a factory method typically works and why it’s useful:

    1. Abstraction of Object Creation: A factory method abstracts the object creation process. Instead of instantiating 
    an object directly using a constructor (like MyClass()), a factory method (like MyClass.create()) is called. 
    This provides a more readable and descriptive way to create objects.

    2. Parameterization: Factory methods can take parameters and use these parameters to decide which class or 
    configuration of the class to instantiate. This allows for a lot of flexibility since the exact type and 
    configuration of the object can be determined at runtime.

    3. Customization: They can be overridden by subclasses if you want to instantiate subclass-specific versions of the 
    class. This means that the factory method in a base class doesn't need to know about the classes of the objects it 
    creates, which is a principle of good design (open/closed principle).

    4. Simplification: They can simplify the creation of complex objects that may require a lot of setup. 
    By encapsulating the creation logic in a method, the client code is shielded from these complexities.
    
"""


class Vehicle:
    def __init__(self, wheels, engine_type):
        self.wheels = wheels
        self.engine_type = engine_type

    @classmethod
    def motorcycle(cls):
        return cls(2, 'petrol')

    @classmethod
    def car(cls):
        return cls(4, 'diesel')

    @classmethod
    def from_parameters(cls, wheels, engine_type):
        if wheels == 2 and engine_type == 'petrol':
            return cls.motorcycle()
        elif wheels == 4 and engine_type == 'diesel':
            return cls.car()
        else:
            return cls(wheels, engine_type)  # Generic vehicle


# Use the factory methods
motorcycle = Vehicle.motorcycle()
car = Vehicle.car()
custom_vehicle = Vehicle.from_parameters(6, 'electric')

"""

Static methods are used when some processing is related to the class but does not need the class or its instances to
 perform any work. They are typically utility functions that perform a task in isolation.

Here's a detailed explanation of why and when to use staticmethod:

    1. Logical Association: Static methods are used when we need a function that has a logical association with the class 
    but does not need to access any class-specific data.

    2. Namespacing: They provide a way to namespace our methods. It's a means of organizing our code and keeping it all 
    in one place. The method is bound to the class it's defined in, not to an instance of the class.

    3. No Implicit Arguments: Since static methods don't take a self or cls parameter, they can't modify object instance 
    state or class state. This is useful for creating utility functions that do not alter the state of the object.

    4. Performance: There's a very slight performance boost with static methods because there is no need to instantiate a 
    bound method (no self or cls is passed), which makes calling a static method slightly faster.

    5. Inheritance: Static methods can be overridden by subclasses, which can be useful if you have a utility method that 
    you want to behave differently in a subclass.

"""


class Mathematics:

    @staticmethod
    def add_numbers(x, y):
        return x + y

    @staticmethod
    def multiply_numbers(x, y):
        return x * y


# Use the static methods
sum_result = Mathematics.add_numbers(5, 10)  # 15
product_result = Mathematics.multiply_numbers(5, 10)  # 50
