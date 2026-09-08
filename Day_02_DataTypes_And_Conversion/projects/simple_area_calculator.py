"""
=========================
Project 3 — Simple Area Calculator

Objective:
Build an interactive program that calculates areas of basic shapes.

Functional Requirements:
- Allow the user to provide dimensions for: rectangle, square, circle
- Calculate the corresponding areas

Expected Features:
- Decimal input
- Correct conversion
- Clear calculation results
- Proper output formatting
=========================
"""

print("===== Simple Area Calculator =====")

print()

# Here We Check Area For Rectangle
length = float(input("Enter length : "))
width = float(input("Enter width : "))
area_of_rect = length * width
print("Area of rectangle :", area_of_rect)

print()

# Here We Check Area For Square
side = float(input("Enter side : "))
area_of_square = side * side
print("Area of square :", area_of_square)

print()

# Here We Check Area For Circle
radius = float(input("Enter radius : "))
area_of_circle = 3.14 * radius * radius
print("Area of circle :", area_of_circle)

print()
print("==================================")
