"""
Project 2 — Student Information Card

Objective:
Build a small student information program.

Functional Requirements:
Store:
- student name
- age
- roll number
- city
- marks
- maximum marks

Expected Features:
- Use multiple assignment
- Use at least one constant
- Display each piece of information
- Display the type of each value
- Follow Python naming standards
- Include documentation
"""

print("===== STUDENT INFORMATION CARD =====")
stu_name, age, roll_number, city, marks, MAX_MARKS = (
    "Nandini",
    25,
    101,
    "Dehradhun",
    98.23,
    100,
)
print("Student Name :", stu_name, type(stu_name))
print("Student Age  :", age, type(age))
print("Roll Number  :", roll_number, type(roll_number))
print("City         :", city, type(city))
print("Marks        :", marks, type(marks))
print("MAX MARKS    :", MAX_MARKS, type(MAX_MARKS))
print("=======================================")
