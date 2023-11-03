"""

Recursion is a programming technique where a function calls itself in order to solve a problem.
Recursion is particularly useful for tasks that can be broken down into similar subtasks, such as searching and sorting
algorithms, traversing trees, and so on.

"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # return the (unchanged) node pointer
    return root


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


# Driver program to test the above functions

#       50
#     /    \
#    30    70
#    / \  / \
#  20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print in order traversal of the BST
inorder(r)
