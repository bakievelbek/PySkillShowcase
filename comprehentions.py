"""

List comprehensions, tuple comprehensions (more accurately called generator expressions), and dictionary comprehensions
are syntactic constructs in Python for creating lists, tuples, and dictionaries from iterables in a clear and concise
way. They allow for the expression of complex loops and filters in a single line of code. Below is an explanation
of each:

"""

"""

List Comprehensions:
A list comprehension provides a way to construct a list in a single line of code. It consists of brackets containing 
an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning 
you can put in all kinds of objects in lists.

The syntax is:

[expression for item in iterable if condition]

"""

# Here is an example of a list comprehension that takes the squares of all even numbers from 0 to 9:

squares_of_even = [x ** 2 for x in range(10) if x % 2 == 0]

"""

Tuple Comprehensions:
Python does not have a dedicated tuple comprehension. However, you can create something similar by using generator 
expressions. A generator expression is similar to a list comprehension, but it uses parentheses instead of square 
brackets. It doesn't create a tuple in one go, but rather an iterator that generates the items on the fly.

The syntax is:

(expression for item in iterable if condition)

"""

# To actually create a tuple from a generator expression, you need to pass it to the tuple() constructor:

squares_of_even = tuple(x ** 2 for x in range(10) if x % 2 == 0)

"""

Dictionary Comprehensions:
Dictionary comprehensions are similar to list comprehensions, but they construct a dictionary. The syntax uses curly 
braces {} instead of square brackets []. Dictionary comprehensions have a key: value pair in the expression.

The syntax is:

{key_expression: value_expression for item in iterable if condition}


"""

# Here is an example of a dictionary comprehension that creates a dictionary with numbers as keys and their squares
# as values:

squares_dict = {x: x ** 2 for x in range(10)}
