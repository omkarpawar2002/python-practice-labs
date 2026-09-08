"""
=========================
Project 2 — Student Profile Generator

Objective:
Build a simple student profile generator.

Functional Requirements:
- Collect: student name, age, roll number, percentage, city
- Display a student profile

Expected Features:
- Correct numeric conversions
- Profile-style output
- Display appropriate data types
- User-friendly prompts
=========================
"""

print("===== Student Profile Generator =====")

student_name = input("Enter your name : ")
age = int(input("Enter your age : "))
roll_number = int(input("Enter your roll number : "))
percentage = float(input("Enter your percentage : "))
city = input("Enter your city : ")

print()

print("Student Name :", student_name)
print("Age          :", age)
print("Roll Number  :", roll_number)
print("Percentage   :", percentage)
print("City         :", city)

print()

# Here We Check Type Of Each Input
print("Student Name Type :", type(student_name))
print("Age Type          :", type(age))
print("Roll Number Type  :", type(roll_number))
print("Percentage Type   :", type(percentage))
print("City Type         :", type(city))

print("=====================================")
