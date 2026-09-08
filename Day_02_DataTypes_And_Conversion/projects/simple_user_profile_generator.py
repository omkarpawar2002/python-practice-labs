"""
=========================
Project 5 — Simple User Profile Generator

Objective:
Build a more complete User Profile Generator using the data types learned so far.

Functional Requirements:
- Collect information: full name, age, height, weight, city, account status, profile-related value that can initially be None
- Convert numeric inputs to appropriate types

Expected Features:
- Interactive profile creation
- Appropriate data types
- Clear profile display
- Type information for profile fields
- Demonstration of None
- At least one numeric calculation
- Professional, readable output

Important Restriction:
Build the project only with concepts learned so far.
Do not add advanced concepts that have not yet been taught.
=========================
"""

print("===== Simple User Profile Generator =====")
print()

full_name = input("Enter Full Name Here : ")
age = int(input("Enter Your Age : "))
height = float(input("Enter Height Here : "))
weight = float(input("Enter Weight Here : "))
city = input("Enter City Name : ")
account_status = input("Is Your Account Active ? (yes / no) ")
number_of_post = None

print()

print("Full Name       :", full_name)
print("Age             :", age)
print("Height          :", height, "inch")
print("Weight          :", weight, "kg")
print("City            :", city)
print("Account status  :", account_status)
print("Number of posts :", number_of_post)

print()
print("=========================================")
