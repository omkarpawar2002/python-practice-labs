"""
=========================
Project 2 — Student Result Analyzer
Difficulty: Beginner

Objective:
Create a small program that analyzes a student's marks using comparison and logical expressions.

Functional Requirements:
- Store marks for several subjects
- Calculate a total
- Calculate an average
- Determine whether marks fall within valid ranges
- Determine whether the student satisfies defined eligibility conditions

Expected Features:
- Total calculation
- Average calculation
- Valid-range checking
- Boolean eligibility result
- Clear output labels
=========================
"""

print("===== Student Result Analyzer =====")
print()

physics = int(input("Enter physics marks : "))
chemistry = int(input("Enter chemistry marks : "))
biology = int(input("Enter biology marks : "))
english = int(input("Enter english marks : "))
computer_science = int(input("Enter computer science marks : "))

total_marks = physics + chemistry + biology + english + computer_science
avg = total_marks / 5
print()

print("Total Marks =", total_marks)
print("Average =", avg)

valid_range = 0 <= avg <= 100
print("Is marks in valid range ?", valid_range)

eligible_for_schoolarship = avg >= 60
print("Eligible For Scholarships :", eligible_for_schoolarship)

print()
print("===================================")
