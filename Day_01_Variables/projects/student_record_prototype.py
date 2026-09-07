"""
Project 5 — Student Record Prototype

Objective:
Build a clean prototype of the data portion of a student-management application.

Functional Requirements:
Create a student record containing:
- student name
- student ID
- age
- city
- course name
- marks
- maximum marks
- academic year
- institution name

Include appropriate constants such as information that is intended to remain fixed.

Expected Features:
The program should:
- Begin with a documentation string
- Use clean variable names
- Follow snake_case
- Use uppercase names for intended constants
- Use multiple assignment somewhere appropriate
- Display the student's information
- Display relevant types using type()
- Demonstrate object identity with id()
- Demonstrate reassignment
- Demonstrate a mutable shared reference
- Contain useful comments
- Follow the PEP 8 basics covered today
- Avoid unnecessary complexity
"""

stu_name = "Arvind"
stu_id = 1001
age = 23
city, course_name = "Delhi", "AI/ML"
course_name = "Python Full Stack"
marks = 78
MAXIMUM_MARKS = 100  # Max Marks Always Constant
academic_year = 2
INSTITUTION_NAME = "Delhi AIIMS"

print("Student Name :", stu_name, type(stu_name), id(stu_name))
print("Student Id :", stu_id, type(stu_id), id(stu_id))
print("Age :", age, type(age), id(age))
print("City :", city, type(city), id(city))
print("Course Name :", course_name, type(course_name), id(course_name))
print("Marks :", marks, type(marks), id(marks))
print("Maximum Marks :", MAXIMUM_MARKS, type(MAXIMUM_MARKS), id(MAXIMUM_MARKS))
print("Academic Year :", academic_year, type(academic_year), id(academic_year))
print(
    "Institution Name :", INSTITUTION_NAME, type(INSTITUTION_NAME), id(INSTITUTION_NAME)
)

languages = ["python", "java", ".net"]
languages_copy = languages
languages_copy.append("C++")

print(languages, type(languages), id(languages))
print(languages_copy, type(languages_copy), id(languages_copy))
