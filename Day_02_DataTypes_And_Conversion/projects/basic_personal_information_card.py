"""
=========================
Project 1 — Basic Personal Information Card

Objective:
Collect basic information from a user and display a simple information card.

Concepts Used:
str, int, input(), print(), explicit conversion

Functional Requirements:
- Ask the user for: name, age, city
- Convert age to an integer
- Display the information clearly

Expected Features:
- Interactive input
- Correct age type
- Clean output
- Clear labels
=========================
"""

print("======== Personal Information Card ========")

name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")

print("Name :", name)
print("Age  :", age)
print("City :", city)

print("Type of age :", type(age))

print("===========================================")
