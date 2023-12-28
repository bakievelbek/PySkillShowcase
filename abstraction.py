from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Now, you cannot create an instance of Shape, but you can create an instance of Rectangle.
rect = Rectangle(10, 5)
print(rect.area())  # 50
print(rect.perimeter())  # 30

"""

Declaring a class with methods that just pass, as in your example, does not make it an abstract class in the strict 
sense used in Python's abc module. Here are the key differences between the two approaches:

"""


# Without Abstract Base Class:

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


"""
    Instantiation: With this definition, Shape can be instantiated. This means you can create an instance of Shape even 
    though it doesn't provide any meaningful implementation for area and perimeter.

    No Enforcement: There is no enforcement of the implementation of the area and perimeter methods in subclasses. A 
    subclass can be created without defining these methods, which might lead to unexpected behaviors if these methods
    are called.

    Intended for Inheritance: Although this class is likely intended to be a base class for inheritance, it doesn't 
    enforce any contract for the derived classes.

"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



"""

    Cannot Be Instantiated: An abstract class cannot be instantiated directly. Attempting to instantiate Shape would 
    result in an error. This enforces the idea that Shape is only a blueprint for other classes.

    Method Enforcement: The use of @abstractmethod decorator requires that any subclass of Shape must implement the 
    area and perimeter methods. If a subclass does not implement these methods, it cannot be instantiated. This enforces 
    a contract that must be followed by derived classes.

    Clear Intent: The use of the abc module and the @abstractmethod decorator makes it clear to other developers that 
    this class is intended to be an abstract base class and that certain methods are expected to be implemented by any 
    non-abstract subclass.
"""
