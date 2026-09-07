"""
Project 4 — Reference & Identity Laboratory

Objective:
Build a small experimental program whose purpose is to investigate how Python variables refer to objects.

Functional Requirements:
Your program should demonstrate:
- Two names referring to an object
- Their types
- Their IDs
- Reassignment of one name
- A mutable object shared by two names
- Modification of that mutable object
- IDs before and after mutation
- Reassignment of one reference to another object

Expected Features:
- Organize the program into clearly labeled sections using comments
- The output should make it easy for another programmer to understand:
  reference → identity → reassignment → mutation
- Do not depend on specific numerical values returned by id()
"""

data_1 = [10, 20, 30, 40]
data_2 = data_1

print("Reference → Two names pointing to same object")
print("Type data_1:", type(data_1))
print("Type data_2:", type(data_2))
print("ID data_1:", id(data_1))
print("ID data_2:", id(data_2))
print()

print("Mutation → Modify the shared list")
print("Before mutation IDs:", id(data_1), id(data_2))
data_2.append(101)
print("After mutation IDs:", id(data_1), id(data_2))
print("data_1:", data_1)
print("data_2:", data_2)
print()

print("Reassignment → Break the link")
data_1 = "This is string"
print("Type data_1:", type(data_1))
print("Type data_2:", type(data_2))
print("ID data_1:", id(data_1))
print("ID data_2:", id(data_2))
print("data_1:", data_1)
print("data_2:", data_2)
