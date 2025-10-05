# Sets in Python are unordered, mutable collections of unique, immutable elements. They are useful for membership testing, removing duplicates, and mathematical operations.

# 1. Creating Sets
# Use curly braces {} or the set() constructor.

# Empty sets must be created with set(), not {} (which creates a dictionary).

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 2])  # Duplicates are removed: {1, 2, 3}
empty_set = set()

print(fruits)
print(numbers)
print(empty_set)


# 2. Key Properties
# Unordered: No indexing or slicing (elements have no fixed position).

# Mutable: Can add/remove elements.

# Unique Elements: Duplicates are automatically removed.

# Immutable Elements Only: Elements must be hashable (e.g., numbers, strings, tuples). Lists/dictionaries cannot be set elements.

fruits.add("orange")       # Add one element
fruits.update(["kiwi", "mango"])  # Add multiple elements
fruits.remove("banana")    # Remove element (raises KeyError if not found)
fruits.discard("banana")   # Remove (no error if not found)
fruits.pop()               # Remove and return an arbitrary element
fruits.clear()  

print(fruits) 

# Set Operations

A = {1, 2, 3}
B = {2, 3, 4}

# Union: Elements in A or B
A | B  # {1, 2, 3, 4}

# Intersection: Elements in both A and B
A & B  # {2, 3}

# Difference: Elements in A but not in B
A - B  # {1}

# Symmetric Difference: Elements in A or B but not both
A ^ B  # {1, 4}



print(A.issubset(B))    # True if A is a subset of B
print(A.issuperset(B))  # True if A is a superset of B
print(A.isdisjoint(B))  # True if A and B have no common elements


unique_list = list(set([1, 2, 2, 3]))  # [1, 2, 3]

print(unique_list)