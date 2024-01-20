"""

The "walrus operator," introduced in Python 3.8, is a new syntax feature that allows you to assign values to variables

 as part of an expression. Officially known as the Assignment Expression, it is represented by :=. This operator can
 be particularly useful for shortening code and potentially improving performance by avoiding repeated calculations
 or function calls.

"""

# Without the walrus operator
my_list = [1, 2, 3, 4, 5]
n = len(my_list)
if n > 3:
    print(f"The list is long (size {n})")

# With the walrus operator
if (n := len(my_list)) > 3:
    print(f"The list is long (size {n})")

# Without the walrus operator
inputs = list()
current = input("Enter a value: ")
while current != "quit":
    inputs.append(current)
    current = input("Enter a value: ")

# With the walrus operator
inputs = list()
while (current := input("Enter a value: ")) != "quit":
    inputs.append(current)
