"""

1. Singleton Pattern

Purpose: Ensures a class has only one instance and provides a global point of access to it.

Python Example:


"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


"""

2. Observer Pattern

Purpose: Allows an object to publish changes to its state to other objects that depend on it.

Python Example:

"""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        raise NotImplementedError("Subclass must implement abstract method")


class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")


"""

3. Factory Method Pattern

Purpose: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

Python Example:

"""


class Product:
    pass


class ConcreteProductA(Product):
    pass


class ConcreteProductB(Product):
    pass


class Creator:
    def factory_method(self):
        raise NotImplementedError("Subclass must implement abstract method")


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


"""

4. Strategy Pattern

Purpose: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

Python Example:


"""


class Strategy:
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        print("Algorithm A implementation")


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        print("Algorithm B implementation")


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


"""

5. Decorator Pattern

Purpose: Attaches additional responsibilities to an object dynamically.

Python Example:

"""


class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        self._component.operation()


class ConcreteDecorator(Decorator):
    def operation(self):
        super().operation()
        self.added_behavior()

    def added_behavior(self):
        print("ConcreteDecorator added behavior")
