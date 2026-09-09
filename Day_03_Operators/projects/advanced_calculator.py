"""
=========================
Project 1 — Advanced Calculator
Difficulty: Very Simple

Objective:
Build a calculator that performs different arithmetic calculations on two numbers.

Functional Requirements:
- Work with two predefined numeric values
- Calculate: addition, subtraction, multiplication, division, floor division, remainder, exponentiation

Expected Features:
- Clearly labeled results
- Separate result for every arithmetic operation
- Correct handling of the different arithmetic operators
=========================
"""

print("===== Advanced Calculator =====")

print()

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponent = num1**num2

print()

print("Addition       : ", addition)
print("Subtraction    : ", subtraction)
print("Multiplication : ", multiplication)
print("Division       : ", division)
print("Floor Division : ", floor_division)
print("Modulus        : ", modulus)
print("Exponent       : ", exponent)

print()
print("===============================")
