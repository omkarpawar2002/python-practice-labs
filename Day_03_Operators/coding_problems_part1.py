# 1. Write a Python program that stores two numbers in variables and prints their sum.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Sum =", n1 + n2)

# 2. Store two numbers and print the result of subtracting the second from the first.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Subtraction =", n1 - n2)

# 3. Store a product price and quantity in variables and calculate the total price.
product_price = float(input("Enter product price : "))
quantity = int(input("Enter quantity : "))
total_price = product_price * quantity
print("Total Price =", total_price)

# 4. Store two numbers and print their division result using /.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Division =", n1 / n2)

# 5. Write a program that stores a number and prints its remainder when divided by 5.
number = int(input("Enter first number : "))
print("Remainder =", number % 5)

# 6. Store two integers and calculate their floor division result.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Floor Division =", n1 // n2)

# 7. Store a base and exponent and calculate the power using **.
base = int(input("Enter base : "))
exp = int(input("Enter exponent : "))
print(base**exp)

# 8. Store a positive number and create another value containing its negative using a unary operator.
num = int(input("Enter any number : "))
num = -num
print("Number =", num)

# 9. Store two numbers and print whether they are equal.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(n1 == n2)

# 10. Store two numbers and print whether the first number is greater than the second.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(n1 > n2)

# 11. Given two numbers, calculate and print addition, subtraction, multiplication, division, floor division, remainder, exponentiation.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("addition =", n1 + n2)
print("subtraction =", n1 - n2)
print("multiplication =", n1 * n2)
print("division =", n1 / n2)
print("floor division =", n1 // n2)
print("remainder =", n1 % n2)
print("exponention =", n1**n2)

# 12. Create a score variable and update it using assignment operators: add 10, subtract 5, multiply by 2, divide by 3.
score = 45
score += 10
score -= 5
score *= 2
score /= 3
print(score)

# 13. Store item price and quantity, then calculate the total amount.
item_price = float(input("Enter item price : "))
quantity = int(input("Enter quantity : "))
print("Total amount =", item_price * quantity)

# 14. Store an integer and use the modulo operator to determine whether it is even.
num = int(input("Enter first number : "))
print(num, "Even =", num % 2 == 0)

# 15. Store a number and check whether it is divisible by 7.
num = int(input("Enter first number : "))
print(num % 7 == 0)

# 16. Store an age and create a Boolean expression that checks whether the person is at least 18.
age = int(input("Enter age : "))
print(age >= 18)

# 17. Store a number and check whether it lies between 10 and 50, inclusive.
num = int(input("Enter number : "))
print(10 <= num <= 50)

# 18. Store age and has_permission, then create an expression that is true only when the person is at least 18 and has permission.
age = int(input("Enter age : "))
has_permission = True
print(age >= 18 and has_permission)

# 19. Store two Boolean values and determine whether at least one of them is true.
has_id = True
is_student = False
print("School Entry ?", has_id or is_student)

# 20. Store a Boolean value and create its opposite using not.
is_student = False
print(not is_student)

# 21. Create a list of five numbers and check whether a particular number exists inside it.
number_list = [10, 45, 33, 78, 23]
print(55 in number_list)

# 22. Store a person's name and check whether the letter "a" occurs in the name.
person_name = input("Enter your name : ")
print("a" in person_name)

# 23. Create a list of allowed countries and check whether a specified country is not present.
allowed_countries = ["India", "Nepal", "Dubai", "Russia"]
print("Pakistan" not in allowed_countries)

# 24. Create a variable containing None and check whether the variable refers to None using the identity operator.
user = None
print(user is None)

# 25. Create two separate lists containing the same values and test value equality and object identity.
li_1 = [10, 20, 30, 40]
li_2 = [10, 20, 30, 40]
print(li_1 == li_2)
print(li_1 is li_2)

# 26. Store original price and discount percentage, then calculate the discount amount and final price.
price = float(input("Enter price : "))
discount = price * 0.10
final_price = price - discount
print("Discount =", discount)
print("Final Price =", final_price)

# 27. Create two numeric variables and calculate sum, difference, product, quotient, remainder.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print("Sum =", n1 + n2)
print("difference =", n1 - n2)
print("product =", n1 * n2)
print("quotient =", n1 / n2)
print("remainder =", n1 % n2)

# 28. Store a total number of seconds and calculate whole minutes and remaining seconds.
total_seconds = int(input("Enter total number of seconds : "))
minute = total_seconds // 60
remaining_seconds = total_seconds % 60
print("Total Minutes : ", minute)
print("Remaining Seconds : ", remaining_seconds)

# 29. Store three numbers and calculate their average.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
avg = (n1 + n2 + n3) / 3
print("Average =", avg)

# 30. Store a salary and increase it by a specified percentage using arithmetic and assignment operators.
salary = float(input("Enter salary : "))
salary_increse = salary * 0.10
salary += salary_increse
print("Final Salary =", salary)