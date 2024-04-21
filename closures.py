"""

Closures

A closure in Python is a technique that allows the preservation of the state of external variables even
after the outer functions have completed. This is achieved by using nested functions that have access to
the variables of the outer function.

"""


def create_transformer(operation, parameter):
    """A function factory for creating different transformer functions based on the operation and its parameter."""
    if operation == 'add':
        def transformer(data):
            return [x + parameter for x in data]
    elif operation == 'multiply':
        def transformer(data):
            return [x * parameter for x in data]
    return transformer


# Create specific transformers
add_five = create_transformer('add', 5)
multiply_by_three = create_transformer('multiply', 3)

# Example data
data = [1, 2, 3, 4]

# Using the created functions
print(add_five(data))  # Output: [6, 7, 8, 9]
print(multiply_by_three(data))  # Output: [3, 6, 9, 12]
