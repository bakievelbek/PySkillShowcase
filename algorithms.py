"""
Search and sort algorithms examples
"""


# Binary Search Algorithm
# Implementation: Binary search is a fast search algorithm that works on the principle of divide and conquer.
# It is used to find the position of a target value within a sorted array.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


# Sample sorted array and target value
sample_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target_value = 9

# Binary search function call
index = binary_search(sample_array, target_value)
print(f"Index of the target ({target_value}):", index)


# Merge Sort Algorithm
# Implementation: Merge sort is a divide and conquer algorithm that divides the input array into two halves,
# calls itself for the two halves, and then merges the two sorted halves.


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Sample unsorted array
sample_array = [38, 27, 43, 3, 9, 82, 10]

# Merge sort function call
merge_sort(sample_array)
print("Sorted array:", sample_array)


# Quick Sort Algorithm
# Implementation: QuickSort is a divide and conquer algorithm.
# It picks an element as a pivot and partitions the given array around the picked pivot.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Sample unsorted array
sample_array = [21, 4, 1, 3, 9, 20, 25]

# Quick sort function call
sorted_array = quick_sort(sample_array)
print("Sorted array:", sorted_array)


# Depth-First Search (DFS) Algorithm
# Implementation: DFS is an algorithm for traversing or searching tree or graph data structures.
# One starts at the root and explores as far as possible along each branch before backtracking.

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)  # This can represent an action taken at the node.

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited


# Sample graph represented as a dictionary
sample_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS function call starting from node 'A'
visited_nodes = dfs(sample_graph, 'A')
print("Visited nodes in DFS order:", visited_nodes)
