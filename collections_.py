"""
Collections overview in Python
"""

from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict

"""
namedtuple: Easy to access tuple element by argument not by number

    Use-case: When you need a lightweight, immutable data structure without the overhead of defining a full class.
    Example: Representing 2D or 3D points in graphics or computational geometry.
"""

Point2D = namedtuple('Point2D', ['x', 'y'])
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])

point_a = Point2D(3, 4)
point_b = Point3D(3, 4, 5)
# point_a and point_b can now be used throughout the code with clear attribute names.

print(point_a.x)
print(point_a.y)
print(point_b.x)
print(point_b.y)
print(point_b.z)

"""
deque: (Doubly ended queue) optimized list for quicker append and pop. Complexity O(1) for append and pop assignments 
with O(n) time complexity

    Use-case: When you need to efficiently append and pop items from both ends of a container, e.g., implementing 
    a queue or a sliding window.
    Example: Maintaining a list of the last N items seen.
"""

last_five = deque(maxlen=5)
for i in range(10):
    last_five.append(i)
print(last_five)  # Expected: deque([5, 6, 7, 8, 9], maxlen=5)

"""
ChainMap: encapsulates many dictionaries into a single unit and returns a list of dictionaries.
List of dicts compared:
- useful when treating multiple dicts as a single mapping
- does not a copy of dicts -> uses the same memory cells
- look up speed
- available from 3.3

    Use-case: Merging multiple dictionaries without creating a new dictionary.
    Example: Handling configuration from multiple sources.
"""

default_config = {'color': 'red', 'user': 'guest'}
custom_config = {'user': 'admin'}
effective_config = ChainMap(custom_config, default_config)

# The user setting will be fetched from custom_config, while other settings fall back to default_config.


"""
Counter:
    Use-case: Quickly counting items in an iterable.
    Example: Finding the frequency of letters in a word.
"""

word = "mississippi"
mass = [1, 3, 4, 5, 3, 4, 1]
letter_counts = Counter(word)
mass_counts = Counter(mass)
print(letter_counts)  # Expected: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

"""
OrderedDict: keeps the same order by which items were inserted

    Use-case: Maintaining the order of items in a dictionary (more relevant in Python versions < 3.7).
    Example: Keeping track of tasks in the order they were added.
"""

tasks = OrderedDict()
tasks['first'] = 'Wake up'
tasks['second'] = 'Brush teeth'
tasks['third'] = 'Exercise'
# Iterating over tasks will always give items in the order: first, second, third.

print(tasks)

"""defaultdict:
Useful when it is required to provide default values for the key that doesn't exists and never raises key error

    Use-case: Needing a dictionary that provides a default value for missing keys, which is especially useful when 
    aggregating data.
    Example: Grouping items by a certain property.
"""

animals = ['cat', 'dog', 'elephant', 'doe', 'eagle']
animal_by_initial = defaultdict(list)
for animal in animals:
    initial = animal[0]
    animal_by_initial[initial].append(animal)
print(animal_by_initial)
# Expected: defaultdict(<class 'list'>, {'c': ['cat'], 'd': ['dog', 'doe'], 'e': ['elephant', 'eagle']})
