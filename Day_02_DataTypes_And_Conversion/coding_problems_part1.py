# 1. Create an integer variable containing your age. Print the value and its type.
age = int(input("Enter your age : "))
print(age, type(age))

# 2. Create a variable containing your height as a decimal number. Print the value and its type.
height = float(input("Enter your height : "))
print(height, type(height))

# 3. Create a complex number representing 3 + 4j. Print the value and its type.
data = 3 + 4j
print(data, type(data))

# 4. Create a string containing your name. Print the value and its type.
name = input("Enter your name : ")
print(name, type(name))

# 5. Create two Boolean variables: one representing that you are a student, one representing that you are employed. Print both values and their types.
is_student = False
is_employee = True
print("Student :", is_student, type(is_student))
print("Employee :", is_employee, type(is_employee))

# 6. Create a variable called result containing None. Print the value and its type.
result = None
print(result, type(result))

# 7. Create one variable of each type: int, float, complex, str, bool, NoneType. Print each value and its type.
roll_number = 101
marks = 78.34
data = 4 - 3j
name = "Kaushik"
is_student = True
result = None
print(roll_number, type(roll_number))
print(marks, type(marks))
print(data, type(data))
print(name, type(name))
print(is_student, type(is_student))
print(result, type(result))

# 8. Use print() to display your name, age, city, and favorite number on separate lines.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")
favourite_number = int(input("Enter your favourite number : "))
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Favourite Number :", favourite_number)

# 9. Create three variables: name, age, city. Display all three using a single print() statement.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city name : ")
print(name, age, city)

# 10. Ask the user for their name and display a greeting.
name = input("Enter your name : ")
print("Welcome,", name)

# 11. Ask the user for their age. Convert the input to an integer and display the value and its type.
age = int(input("Enter your age : "))
print(age, type(age))

# 12. Ask the user for their height. Convert it to float and display the value and type.
height = float(input("Enter your height : "))
print(height, type(height))

# 13. Ask the user for two integers. Display their sum.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Sum =", n1 + n2)

# 14. Ask the user for two decimal numbers. Display their sum.
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print("Floating addition =", num1 + num2)

# 15. Start with "100". Convert it into an integer and display the original value, converted value, and converted type.
data = "100"
print(data, type(data))
data = int(data)
print(data, type(data))

# 16. Convert "45.75" into a float. Display its value and type.
value = "45.75"
value = float(value)
print(value, type(value))

# 17. Create an integer containing your age. Convert it to a string and display its type before and after conversion.
age = int(input("Enter your age : "))
print(age, type(age))
age = str(age)
print(age, type(age))

# 18. Ask the user for name, age, and city. Convert the age to an integer and display all information.
name = input("Enter name : ")
age = int(input("Enter age : "))
city = input("Enter city : ")
print("Name :", name, "\nAge :", age, "\nCity :", city)

# 19. Ask the user for student name, roll number, and percentage. Use appropriate data types and display all information with types.
stu_name = input("Enter your name : ")
roll_number = int(input("Enter your roll number : "))
percentage = float(input("Enter your percentage : "))
print("Student Name :", stu_name, type(stu_name))
print("Roll Number :", roll_number, type(roll_number))
print("Percentage :", percentage, type(percentage))

# 20. Ask the user for product name, quantity, and price. Convert quantity to int and price to float. Display all three.
product_name = input("Enter product name : ")
quantity = int(input("Enter quantity : "))
price = float(input("Enter price : "))
print("Product Name :", product_name)
print("Product Quantity :", quantity)
print("Product Price :", price)

# 21. Ask the user for length and width. Convert both to floats and calculate the area of a rectangle.
length = float(input("Enter length : "))
width = float(input("Enter width : "))
print("Area of rectangle =", length * width)

# 22. Ask the user for the side of a square. Convert it to a numeric type and calculate the area.
side = int(input("Enter side : "))
print("Area of square :", side**2)

# 23. Ask the user for two numbers. Convert both to integers and display their sum. Then display the result's type.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Sum =", n1 + n2)
print(type(n1 + n2))

# 24. Ask the user for two decimal values. Convert them to floats and display their sum and type.
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
sum = num1 + num2
print("Total =", sum)
print(type(sum))

# 25. Ask the user for name, age, and height. Store them using appropriate types. Display each value and its type.
name = input("Enter name here : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
print("Name :", name, type(name))
print("Age :", age, type(age))
print("Height :", height, type(height))
