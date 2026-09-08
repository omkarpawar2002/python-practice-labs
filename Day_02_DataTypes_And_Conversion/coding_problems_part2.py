# 26. Ask the user for the radius of a circle. Convert it to float, calculate the area using π, and display the result.
radius = float(input("Enter radius : "))
area = 3.14 * radius * radius
print("Area of circle :", area)

# 27. Ask the user for principal, rate, and time. Convert inputs appropriately and calculate simple interest.
principal = int(input("Enter principal amount : "))
rate = float(input("Enter rate of interest : "))
time = int(input("Enter time period : "))
print("Simple Interest : ", (principal * rate * time) / 100)

# 28. Ask the user for a Celsius temperature. Convert it to float and calculate Fahrenheit.
celcius_temperature = float(input("Enter celsius temperature : "))
fahrenheit = (9 / 5) * celcius_temperature + 32
print("Fehrenheit =", fahrenheit)

# 29. Ask the user for three numbers. Convert them to floats and calculate their average. Display the result and its type.
n1 = float(input("Enter first number : "))
n2 = float(input("Enter second number : "))
n3 = float(input("Enter third number : "))
avg = (n1 + n2 + n3) / 3
print("Average : ", avg, type(avg))

# 30. Ask the user for the prices of three products. Convert each to float and calculate the total.
product_1 = float(input("Enter product 1 price : "))
product_2 = float(input("Enter product 2 price : "))
product_3 = float(input("Enter product 3 price : "))
print("Total =", (product_1 + product_2 + product_3))

# 31. Ask for name, age, height, and account status. Use str, int, float, and bool. Display the complete profile and each value's type.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
is_account_active = False
print("Name :", name, type(name))
print("Age :", age, type(age))
print("Height :", height, type(height))
print("Is Account Active ? ", is_account_active, type(is_account_active))

# 32. Start with "250". Convert string → integer → float → string. Display the value and type after each stage.
data = "250"
print(data, type(data))
data = int(data)
print(data, type(data))
data = float(data)
print(data, type(data))

# 33. Create one integer, one float, and one complex number. Display their values and types. Perform operations between compatible values.
age = int(input("Enter your age : "))
percentage = float(input("Enter your percentage ; "))
data = 4 + 4j
print(age, type(age))
print(percentage, type(percentage))
print(data, type(data))
print(age + percentage, type(age + percentage))

# 34. Create an integer and a float. Add them together. Display both original types, the result, and the result type.
id = int(input("Enter id : "))
price = float(input("Enter price : "))
total = id + price
print("Id :", id, type(id))
print("Price :", price, type(price))
print("Total :", total, type(total))

# 35. Ask the user for a number. Display the type returned directly by input(). Then convert to integer and display the new type.
num = input("Enter number : ")
print(num, type(num))
num = int(num)
print(num, type(num))

# 36. Ask the user for a product price as input. Convert the value to float and then to string. Display the value and type at each stage.
product_price = float(input("Enter price : "))
print(product_price, type(product_price))
product_price = str(product_price)
print(product_price, type(product_price))

# 37. Ask the user for distance traveled and number of hours. Convert both to floats and calculate average speed.
distance_travelled = float(input("Distance Travelled : "))
number_of_hours = float(input("Enter number of hours : "))
avg = distance_travelled / number_of_hours
print(avg)

# 38. Ask for employee name, employee ID, and monthly salary. Use appropriate types and display the information with its types.
employee_name = input("Enter your name : ")
employee_id = int(input("Enter employee id : "))
salary = float(input("Enter salary : "))
print("Employee Name :", employee_name)
print("Employee Id :", employee_id)
print("Employee Salary :", salary)

# 39. Ask for item price and quantity. Convert appropriately. Calculate the total bill and display price, quantity, total, and types.
item_price = float(input("Enter item price : "))
quantity = int(input("Enter quantity : "))
total = item_price * quantity
print("Item Price :", item_price, type(item_price))
print("Quantity :", quantity, type(quantity))
print("Total :", total, type(total))

# 40. Create an interactive profile that asks for name, age, height, and favorite number. Use appropriate types and print a formatted profile.
name = input("Enter name : ")
age = int(input("Enter age : "))
height = float(input("Enter height : "))
favourite_number = int(input("Enter favourite number : "))
print("==============================")
print("Name :", name)
print("Age :", age)
print("Height :", height)
print("Favourite Number :", favourite_number)
print("===============================")

# 41. Accept student name, roll number, and three subject marks. Calculate total and average. Display all information and data types.
student_name = input("Enter name here : ")
roll_number = int(input("Enter roll number : "))
subject1 = int(input("Enter subject1 marks : "))
subject2 = int(input("Enter subject2 marks : "))
subject3 = int(input("Enter subject3 marks : "))
total = subject1 + subject2 + subject3
print("Subject 1 marks : ", subject1, type(subject1))
print("Subject 2 marks : ", subject2, type(subject2))
print("Subject 3 marks : ", subject3, type(subject3))
print("Student Name : ", student_name, type(student_name))
print("Roll Number : ", roll_number, type(roll_number))
print("Total =", total)
print("Average =", (total / 3))

# 42. Ask the user for dish name, price, and quantity. Calculate the total bill and display the result clearly.
dish_name = input("Enter dish name : ")
price = float(input("Enter price : "))
quantity = int(input("Enter quantity : "))
print("Dish Name :", dish_name)
print("Total bill =", price * quantity)

# 43. Ask the user for starting distance, additional distance, and number of travel hours. Calculate total distance and average speed.
starting_distance = float(input("Enter starting distance : "))
additional_distance = float(input("Enter additional distance : "))
number_of_hours = float(input("Number of hours : "))
total_distance = starting_distance + additional_distance
avg = total_distance / number_of_hours
print("Total distance =", total_distance)
print("Average speed =", avg)

# 44. Collect employee name, employee ID, age, salary, and height. Display a complete profile with the type of every field.
emp_name = input("Enter employee name : ")
emp_id = int(input("Enter employee id : "))
age = int(input("Enter age : "))
salary = float(input("Enter salary : "))
height = float(input("Enter height : "))
print("Employee Name :", emp_name, type(emp_name))
print("Employee Id :", emp_id, type(emp_id))
print("Age :", age, type(age))
print("Salary :", salary, type(salary))
print("Height :", height, type(height))

# 45. Ask the user for a product price. Display original input type, converted float, converted integer, and converted string.
product_price = input("Enter product price : ")
print(product_price, type(product_price))
product_price = float(product_price)
print(product_price, type(product_price))
product_price = int(product_price)
print(product_price, type(product_price))
product_price = str(product_price)
print(product_price, type(product_price))

# 46. Ask the user for dimensions and calculate rectangle area, square area, and circle area. Use appropriate numeric conversions.
radius = float(input("Enter radius : "))
side = int(input("Enter side : "))
length = float(input("Enter length : "))
width = float(input("Enter width : "))
print("Area of circle :", (3.14 * radius * radius))
print("Area of square :", (side * side))
print("Area of rectangle :", length * width)

# 47. Create a program using integers, floats, and complex numbers. Perform operations and display the result and result type. Show automatic numeric conversion.
num1 = int(input("Enter first number : "))
num2 = float(input("Enter second number : "))
data = 4 - 4j
result = num1 + num2
print("Result =", result, type(result))

# 48. Ask the user for full name, age, height, weight, city, and account status. Store each using appropriate type and print a complete report.
full_name = input("Enter full name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
weight = float(input("Enter your weight : "))
city = input("Enter city name : ")
account_active = False
print("Full Name :", full_name)
print("Age :", age)
print("Height :", height)
print("Weight :", weight)
print("City :", city)
print("Account Active :", account_active)

# 49. Ask for customer name, product name, quantity, price, and payment amount. Convert numeric inputs, calculate purchase total and remaining amount, and display all information.
customer_name = input("Enter customer name : ")
product_name = input("Enter product name : ")
quantity = int(input("Enter quantity : "))
price = float(input("Enter product price : "))
payment_amount = float(input("Enter payment amount : "))
print("Customer Name :", customer_name)
print("Product Name :", product_name)
print("Purchase total :", quantity * price)
print("Remaining amount :", payment_amount)

# 50. Build a program that asks for different kinds of information using str, int, float, complex, bool, and None. Display every value and its type. Include one explicit type conversion and one numeric calculation.
first_name = input("Enter first name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
data = 4 - 2j
is_student = True
result = None
print("First Name : ", first_name, type(first_name))
print("Age :", age, type(age))
print("Height :", height, type(height))
print("data :", data, type(data))
print("Is student :", is_student, type(is_student))
print("Result :", result, type(result))