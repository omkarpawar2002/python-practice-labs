# 1. Create a variable named name and assign your name to it.
name = "Ankit"
print(name)

# 2. Create a variable called age and store an integer representing your age.
age = 25
print(age)

# 3. Create three variables: name, age, city. Store appropriate values and print all three.
name = "Shreeleela"
age = 26
city = "Tamilnadu"
print("Name :", name)
print("Age :", age)
print("City :", city)

# 4. Create variables for student name, student age, student marks. Print each variable on a separate line.
student_name = "Keshav"
student_age = 18
student_marks = 78
print(student_name)
print(student_age)
print(student_marks)

# 5. Create a variable containing a person's name. Use type() to print its type.
person_name = "Anuj"
print(type(person_name))

# 6. Create a variable containing an integer. Use type() to inspect it.
age = 23
print(type(age))

# 7. Create variables: name, age, height. Use type() on all three.
name = "Anuja"
age = 19
height = 7.5
print(type(name))
print(type(age))
print(type(height))

# 8. Create a constant named MAX_SCORE. Assign an appropriate value. Print it.
MAX_SCORE = 100
print(MAX_SCORE)

# 9. Write a short program containing one variable, one useful comment, and one print() statement.
score = 98  # Student score 98 out of 100
print(score)

# 10. Create a small Python program that begins with a documentation string. Then create at least two variables.
"""This is a documentation string in python"""
age = 23
name = "Ovi"
print(name, age)

# 11. Create first_name and last_name. Assign values and print both.
first_name = "Stiphen"
last_name = "Kelvin"
print("First Name :", first_name)
print("Last Name :", last_name)

# 12. Create variables for name, age, city, country. Print each variable.
name = "Arvind"
age = 28
city = "Pune"
country = "Bharat"
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Country :", country)

# 13. Create score = 50. Print it. Then change the variable to 100 and print it again.
score = 50
print(score)
score = 100
print(score)

# 14. Create a variable called value. First assign an integer to it. Then assign a string to the same variable. Use type() after each assignment.
value = 120
print(type(value))
value = "Kishan"
print(type(value))

# 15. Create three variables: name, age, city. Assign all three using a single multiple-assignment statement. Then print them.
name, age, city = "Rohini", 23, "Pune"
print(name, age, city)

# 16. Create x, y, z. Assign the same value to all three using a single assignment statement. Print all three.
x = y = z = 100
print(x, y, z)

# 17. Create a = 10, b = 20. Swap their values using Python's multiple-assignment syntax. Print both after the swap.
a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

# 18. Create a, b, c. Assign different values. Rotate their values so that a receives b's original value, b receives c's original value, c receives a's original value.
a, b, c = 100, 200, 300
print(a, b, c)
a, b, c = b, c, a
print(a, b, c)

# 19. Create x = 100. Print x, type(x), id(x).
x = 100
print(x, type(x), id(x))

# 20. Create x = 100, y = x. Print id(x), id(y).
x = 100
y = x
print(id(x))
print(id(y))

# 21. Create x, y. Make both refer to the same value. Then reassign x to another value. Print x, y, id(x), id(y).
x = 100
y = x
x = 200
print(x, y)
print(id(x))
print(id(y))

# 22. Create constants representing maximum score, minimum passing score, number of months in a year. Print them.
MAXIMUM_SCORE = 100
MINIMUM_SCORE = 20
NUMBER_OF_MONTHS_IN_YEAR = 12
print("Maximum Score :", MAXIMUM_SCORE)
print("Minimum Score :", MINIMUM_SCORE)
print("Number Of Months In Year :", NUMBER_OF_MONTHS_IN_YEAR)

# 23. Rewrite invalid or poor names into valid Python identifiers: 1student, student name, class, studentMarks, x. Then create variables using your corrected names.
"""
1student, student name, class, studentMarks, x

This are the invalid or not recommended variable names
"""
student1 = "ankit"
student_name = "Pallavi"
school_class = 8
student_marks = 76
school_fees = 12000
print(student1)
print(student_name)
print(school_class)
print(student_marks)
print(school_fees)

# 24. Create variables for city name, current temperature, maximum temperature, minimum temperature. Print all values.
city_name = "Pune"
current_temperature = 18.9
MAXIMUM_TEMPERATURE = 100
MINIMUM_TEMPERATURE = 0
print(city_name)
print(current_temperature)
print(MAXIMUM_TEMPERATURE)
print(MINIMUM_TEMPERATURE)

# 25. Create variables for product name, product price, product quantity, product code. Print each value and its type.
product_name = "Laptop"
product_price = 70000.00
product_quantity = 5
product_code = "#FFF23540ZXR"
print("Product Name :", product_name, type(product_name))
print("Product Price :", product_price, type(product_price))
print("Product Quantity :", product_quantity, type(product_quantity))
print("Product Code :", product_code, type(product_code))