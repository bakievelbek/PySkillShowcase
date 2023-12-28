"""

Metaclasses in Python are a somewhat advanced and specialized feature. They are classes of classes; that is, they
define how classes behave, rather than instances of classes. Metaclasses are used to control the creation, modification,
and deletion of classes.
Basic Usage of Metaclasses

A metaclass is defined like any other class in Python, but it usually derives from type, which is the default metaclass
in Python. Metaclasses can override the __new__ or __init__ methods to modify or extend the class creation process.

"""

"""

Practical Usage of Metaclasses

Metaclasses can be used in various ways, such as:

    Validating Subclasses: Ensuring that subclasses meet certain criteria.
    Automatic Resource Management: Such as automatically registering classes in some registry or with certain systems.
    Singleton Pattern Implementation: Ensuring that only one instance of a class exists.
    Logging or Profiling: Automatically adding logging or profiling to methods of a class.

"""


# Defining a metaclass


class Meta(type):
    def __new__(cls, name, bases, dct):
        # custom actions or modifications
        dct['custom_attribute'] = 'Added by Meta'
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        # initialization actions
        super().__init__(name, bases, dct)
        cls.class_attribute = "Initialized by Meta"


"""

In this Meta class:

    __new__ is used to create the class. We add a custom_attribute to every class that uses this metaclass.
    __init__ is used to initialize the class. Here, we add a class_attribute to the class.
    
"""


# Using metaclasses


class MyClass(metaclass=Meta):
    def method(self):
        return "Method in MyClass"


# Usage
instance = MyClass()
print(instance.custom_attribute)  # Outputs: Added by Meta
print(MyClass.class_attribute)  # Outputs: Initialized by Meta


# PURE EXAMPLE

class RequiredMethodsMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if bases != (object,):  # Ignore base class
            required = getattr(cls, "required_methods", [])
            for method in required:
                if not callable(getattr(cls, method, None)):
                    raise TypeError(f"Class {name} lacks required method: {method}")


class PluginBase(metaclass=RequiredMethodsMeta):
    required_methods = ['load', 'save']


class FilePlugin(PluginBase):
    def load(self):
        print("Loading file...")

    def save(self):
        print("Saving file...")


class NetworkPlugin(PluginBase):
    def load(self):
        print("Loading from network...")

    # `save` method is missing here


file_plugin = FilePlugin()  # Works fine
file_plugin.load()  # Outputs: Loading file...

try:
    network_plugin = NetworkPlugin()  # Raises TypeError
except TypeError as e:
    print(e)  # Outputs: Class NetworkPlugin lacks required method: save
