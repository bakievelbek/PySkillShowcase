"""

Slots in Python Classes

Slots are a feature in Python that allows for a more efficient allocation of memory for class instances.
By defining __slots__, you can explicitly declare data members (attributes) of a class and prevent the creation
 of __dict__ and __weakref__ for each instance.

"""

"""

Features and Usage:

    Memory Efficiency: When you have a large number of instances of a class, using __slots__ can result in significant 
    memory savings.

    Faster Attribute Access: Access to slot-based attributes is typically faster than access to __dict__-based 
    attributes.

    Restricting Attributes: __slots__ can also be used to restrict the addition of new attributes to a class, 
    providing a form of attribute encapsulation.

"""


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(p.x, p.y)  # 1 2

# Trying to add a new attribute will result in an AttributeError
# p.z = 3  # AttributeError: 'Point' object has no attribute 'z'


"""

 By default, when Python creates a new instance of a class, it creates a __dict__ attribute for the class. 
 The __dict__ attribute is a dictionary whose keys are the variable names and whose values are the variable values. 
 This allows for dynamic variable creation but can also lead to uncaught errors. For example, with the default __dict__, 
 a misspelled variable name results in the creation of a new variable, but with __slots__
  it raises in an AttributeError. 

"""


class PointWithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Creating an instance
point1 = PointWithDict(1, 2)

# Accessing attributes
print(point1.x, point1.y)  # Outputs: 1 2

# Misspelling an attribute name creates a new attribute
point1.z = 3  # No error; creates a new attribute 'z'
print(point1.z)  # Outputs: 3


class PointWithSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Creating an instance
point2 = PointWithSlots(1, 2)

# Accessing attributes
print(point2.x, point2.y)  # Outputs: 1 2

# Attempting to add a new attribute results in an error
try:
    point2.z = 3
except AttributeError as e:
    print("Error:", e)  # Outputs: Error: 'PointWithSlots' object has no attribute 'z'
