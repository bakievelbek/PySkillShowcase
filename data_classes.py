"""
Key Features of Data Classes

    Automatic Generation of Special Methods: Methods like __init__, __repr__, and __eq__ are automatically created,
    reducing the need for repetitive boilerplate code.
    Type Annotations: Data classes make use of type annotations, providing a clear specification of the attributes
    each class is expected to handle.
    Immutability Option: You can make instances of the class immutable (read-only) by setting the frozen parameter
    to True. Default Values: You can provide default values for the fields, simplifying the creation of class instances.


"""

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    quantity: int = 0


# Creating an instance of the Product class
item = Product(name="Apple", quantity=5)
print(item)  # Output: Product(name='Apple', quantity=5)

"""
Advanced Features

Data classes also support more advanced features:

    Field Customization: You can customize the behavior of each field using the field() function from the dataclasses 
    module, for example, to exclude a field from the generated __repr__ method.
    Post-Initialization Processing: The __post_init__ method can be defined to add additional processing after the 
    standard __init__ method.
    Inheritance: Data classes can be inherited from other data classes. The fields from parent classes are inherited by 
    the child class.
    Comparison Methods: By default, data classes provide comparison methods (__eq__, __lt__, etc.), but you can disable
    or customize this behavior.

"""

breakpoint()


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    total_cost: float = field(init=False)

    def __post_init__(self):
        self.total_cost = self.unit_price * self.quantity_on_hand


item = InventoryItem(name="Orange", unit_price=0.5, quantity_on_hand=100)
print(item)  # Output: InventoryItem(name='Orange', unit_price=0.5, quantity_on_hand=100, total_cost=50.0)
