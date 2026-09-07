# 26. Create variables for name, age, roll number, marks, city. Then print each variable together with its type.
name = "Krushna"
age = 28
roll_number = 101
marks = 78
city = "Mumbai"
print(name, type(name))
print(age, type(age))
print(roll_number, type(roll_number))
print(marks, type(marks))
print(city, type(city))

# 27. Create a variable named data. Assign these values to it one after another: integer, string, floating-point value, boolean. After every assignment, print its value and type.
data = 10
print(data, type(data))
data = "Keshav"
print(data, type(data))
data = 99.99
print(data, type(data))
data = False
print(data, type(data))

# 28. Create a = 50, b = a, c = b. Print values, types, and IDs for all three variables.
a = 50
b = a
c = b
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))

# 29. Create a, b. Make b refer to the object referenced by a. Then reassign a to another value. Display both variables afterward.
a = 100
b = a
a = "rani"
print(a, b)

# 30. Create a list containing three values. Assign the same list to a second variable. Modify the list. Then print both variables.
li = [10, 20, 30]
li_1 = li
li.append(101)
print(li, li_1)

# 31. Create a mutable object and assign it to two variables. Print both IDs. Modify the object's contents. Print both IDs again.
li = [10, 20, 30]
li_1 = li
print(id(li))
print(id(li_1))
li_1.append(101)
print(id(li))
print(id(li_1))

# 32. Create an integer and assign its reference to a second variable. Reassign the first variable. Print both variables and their IDs.
data = 100
data1 = data
data = "name"
print(data, id(data))
print(data1, id(data1))

# 33. Write a program that stores information about an employee using at least five variables. Include at least one constant.
emp_name = "Anuj"
emp_salary = 35000.00
EMP_ID = 101
emp_dept = "Sales"
emp_joined_date = "2025/12/24"
print("Employee Name :", emp_name)
print("Employee Salary :", emp_salary)
print("Employee Id :", EMP_ID)
print("Employee Department :", emp_dept)
print("Employee Joined Date :", emp_joined_date)

# 34. Rewrite this code according to PEP 8 naming and spacing principles: studentName="Alex", student_age=20, MAXmarks=500, totalMarks=450. Then print the corrected variables.
student_name = "Alex"
student_age = 20
MAX_MARKS = 500
total_marks = 450
print("Student Name :", student_name)
print("Student Age :", student_age)
print("Maximum Marks :", MAX_MARKS)
print("Total Marks :", total_marks)

# 35. Create a small program representing a product. Begin with a documentation string. Use at least two useful comments. Create at least five appropriately named variables. Include one constant. Print the information.
"""Here is a product details used for e-commerce website"""
product_category = "Electronics"  # Here we describe product category for our e-commerce
product = "Laptop"
product_price = 80000.00
product_quantity = 20
PRODUCT_BRAND = (
    "ASUS"  # Here this brand always constant because we want to work with only ASUS
)
print("Product Category :", product_category)
print("Product :", product)
print("Product Price :", product_price)
print("Product Quantity :", product_quantity)
print("Product Brand :", PRODUCT_BRAND)

# 36. Create variables containing different kinds of values. Use type() to inspect every variable. Include at least one integer, one string, one floating-point value, and one boolean.
stu_id = 101
print(stu_id, type(stu_id))
name = "kishor"
print(name, type(name))
stu_percentage = 89.23
print(stu_percentage, type(stu_percentage))
is_student = True
print(is_student, type(is_student))

# 37. Create three variables. Assign one variable to another. Assign the second variable to the third. Print all three IDs. Then reassign one variable and print all IDs again.
a, b, c = 100, "welcome", True
a, b, c = b, c, a
a = 34.56
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 38. Create a profile using one multiple-assignment statement. Store name, age, city, country, profession. Then print the values and their types.
name, age, city, country, profession = "Nurr", 21, "Hydrabad", "India", "Sales"
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Country :", country)
print("Profession :", profession)

# 39. Create two variables containing different numbers. Swap them without creating a third temporary variable. Use Python's multiple-assignment feature.
x = 100
y = 200
print(x, y)
x, y = y, x
print(x, y)

# 40. Create variables for customer's first name, customer's account balance, customer's account number, maximum withdrawal amount, minimum account balance. Identify which names should be treated as constants.
customer_first_name = "Alex"
account_balance = 12000
account_number = 123412341234
maximum_withdraw_amt = 10000
MINIMUM_ACCOUNT_BALANCE = 2000
print(customer_first_name, account_balance, account_number)
print("Minimum Balance :", MINIMUM_ACCOUNT_BALANCE)
print("Maximum Withdrawl :", maximum_withdraw_amt)

# 41. Create a basic student information program containing student name, age, roll number, city, total marks, maximum marks. Print every value and its type.
print("==== Student Details ====")
name = "Kaustubh"
age = 21
roll_number = 101
city = "Pune"
total_marks = 92
MAXIMUM_MARKS = 100
print("Name :", name, type(name))
print("Age :", age, type(age))
print("Roll Number :", roll_number, type(roll_number))
print("City :", city, type(city))
print("Total Marks :", total_marks, type(total_marks))
print("Maximum Marks :", MAXIMUM_MARKS, type(MAXIMUM_MARKS))
print("===========================")

# 42. Create several variables referring to the same object. Print their values, types, and IDs. Reassign one variable. Print everything again.
x1 = 100
y1 = x1
z1 = x1
print(x1, type(x1), id(x1))
print(y1, type(y1), id(y1))
print(z1, type(z1), id(z1))
y1 = "welcome"
print(x1, type(x1), id(x1))
print(y1, type(y1), id(y1))
print(z1, type(z1), id(z1))

# 43. Create a program that demonstrates the difference between mutating a mutable object and rebinding a name associated with an immutable object. Print values and IDs before and after the operations.
li_1 = [10, 20, 30]
li_2 = li_1
li_2.append(101)
print(li_1)
print(li_2)

x = 101
y = x
x = "Welcome"
print(x)
print(y)

# 44. Build a basic employee record containing employee name, employee ID, department, salary, years of experience, company name. Print every variable and its type.
employee_name = "Asif"
employee_id = 1001
emp_dept = "IT"
emp_salary = 42000.00
year_of_exp = 4
COMPANY_NAME = "Cognizant"
print(employee_name, type(employee_name))
print(employee_id, type(employee_id))
print(emp_dept, type(emp_dept))
print(emp_salary, type(emp_salary))
print(year_of_exp, type(year_of_exp))
print(COMPANY_NAME, type(COMPANY_NAME))

# 45. Create a product configuration containing product name, product price, stock quantity, product category, maximum stock capacity, company name. Add a documentation string and useful comments.
"""Product Details"""
product_name = "TV"
product_price = 49999.99
stock_quantity = 100
product_category = "Electronics"
MAXIMUM_STOCK_CAPACTIY = 250
company_name = "LG"
print(
    product_name,
    product_price,
    stock_quantity,
    product_category,
    MAXIMUM_STOCK_CAPACTIY,
    company_name,
)

# 46. Create a variable called data. Make it refer to at least five different types one after another. After each reassignment, print the value, type, and ID.
data = 101
print(data, type(data), id(data))
data = 99.99
print(data, type(data), id(data))
data = "welcome"
print(data, type(data), id(data))
data = True
print(data, type(data), id(data))
data = None
print(data, type(data), id(data))

# 47. Create four variables a, b, c, d. Assign four different values. Rotate their values so that a ← original d, b ← original a, c ← original b, d ← original c.
a, b, c, d = 100, 200, 300, 400
print(a, b, c, d)
a, b, c, d = d, a, b, c
print(a, b, c, d)

# 48. Rewrite this poor style code according to principles: studentName="Alex", AGE=20, student_city="Mumbai", marks=450, MAXmarks=500, x=studentName. Improve identifiers, naming conventions, spacing, constants, and add a documentation string. Print the information and types.
"""Student Profile Details"""
student_name = "Alex"
age = 20
student_city = "Mumbai"
marks = 450
MAX_MARKS = 500
x = student_name
print(student_name, type(student_name))
print(age, type(age))
print(student_city, type(student_city))
print(marks, type(marks))
print(MAX_MARKS, type(MAX_MARKS))
print(x, type(x))

# 49. Create a mutable object and assign it to three different variables. Print all three values and IDs. Modify the object. Print values and IDs again. Reassign one variable to a different object. Print all values and IDs one final time.
li = [10, 20, 30]
a = b = c = li
print(a, id(a))
print(b, id(b))
print(c, id(c))
li.append(101)
print(a, id(a))
print(b, id(b))
print(c, id(c))
b = "welcome"
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 50. Build a small Student Profile Information System containing student name, age, city, roll number, course name, marks, maximum marks. Use constants, documentation string, comments, multiple assignment, type(), id(), reassignment, reference relationship, and a mutable reference.
"""===== Student Profile Information System ====="""
stu_name = "Anu"
age = 24
city = "Mumbai"
roll_number = 18
course_name = "Full Stack Python"  # Mandatory To Provie Course Name
marks = 78.35
MAXIMUM_MARKS = 100
print("Stu Name :", stu_name)
print("Age :", age)
print("City :", city)
print("Roll Number :", roll_number)
print("Course Name :", course_name)
print("Marks :", marks)
print("Maximum Marks :", MAXIMUM_MARKS)