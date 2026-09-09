# 31. Store two temperatures and create Boolean expressions that determine whether they are equal, whether the first is hotter, and whether the second is hotter.
temp_1 = float(input("Temperature 1 : "))
temp_2 = float(input("Temperature 2 : "))
print("Temperature 1 Hotter = ", temp_1 >= temp_2)
print("Temperature 2 Hotter = ", temp_2 >= temp_1)

# 32. Store a number and determine whether it is greater than 100 and less than 200.
num = int(input("Enter any number : "))
print(100 <= num <= 200)

# 33. A score must be from 0 through 100. Create an expression that checks whether the score is valid.
score = int(input("Enter score : "))
print("Score is valid :", 0 <= score <= 100)

# 34. Create variables representing correct username status and correct password status, then create a Boolean expression for successful authentication.
username = input("Enter username : ")
password = input("Enter password : ")
authenticate = (username == "admin") and (password == "admin@123")
print("Authentication Successful =", authenticate)

# 35. A user can access a system if they are either an administrator or an authorized employee. Create a logical expression representing this rule.
user_role = input("Enter user role : ")
print("Access System : ", user_role in ["administrator", "employee"])

# 36. Store a day name and determine whether the day is either "Saturday" or "Sunday".
day = input("Enter day here : ")
print(day == "Saturday" or day == "Sunday")

# 37. Create a collection of allowed roles. Given a user's role, determine whether it is allowed.
allowed_roles = ["admin", "superadmin", "employee"]
user_role = input("Enter your role : ")
print("Allowed :", user_role in allowed_roles)

# 38. Create an expression containing addition, subtraction, multiplication, division, exponentiation. Apply Python's precedence rules and print the result.
exp = 10 + 6 / 4 * 4 - 10**2
print(exp)

# 39. Create two mathematically related expressions where adding parentheses changes the result. Print both results.
res1 = 10 + 5 * 2
print("Result :", res1)
res2 = (10 + 5) * 2
print("Result :", res2)

# 40. A person is eligible when their age is between 18 and 60, and they have permission. Create one Boolean expression representing this rule.
age = int(input("Enter your age here : "))
has_permission = input("Do you have permission ? (yes / no) ")
check_eligibility = (age >= 18 and age <= 60) and (has_permission == "yes")
print("Check Eligibility :", check_eligibility)

# 41. A user is eligible if they are an administrator, or they are an employee with permission. Create one Boolean expression representing this requirement.
allowed_roles = ["admin", "employee"]
user = input("Enter your role here : ")
has_permission = input("Do you have permission ? (yes / no) ")
check_eligibility = user == "admin" or (user == "employee" and has_permission == "yes")
print("Eligibile : ", check_eligibility)

# 42. Create a collection of allowed roles. A user is allowed if their role belongs to the allowed roles, and their account is active.
allowed_roles = ["admin", "manager", "superadmin"]
account_active = input("Is your account active ? (yes / no) ")
user_role = input("Enter your role : ")
allowed = user_role in allowed_roles and (account_active == "yes")
print(allowed)

# 43. Create an expression that attempts a division only when the denominator is non-zero using short-circuit evaluation.
numerator = int(input("Enter first number : "))
denominator = int(input("Enter second number : "))
result = (denominator != 0) and (numerator / denominator)
print(result)

# 44. Store a number and determine whether 10 < number < 100 using a chained comparison. Then create an equivalent logical expression using and.
number = int(input("Enter any number : "))
print(10 < number < 100)
using_and = number > 10 and number < 100
print(using_and)

# 45. Create a single expression involving arithmetic, comparison, and logical operators. Use parentheses to make the intended evaluation order clear. The final result must be Boolean.
num = 15
expression = ((10 + 5) == 15) and (num >= 15)
print(expression)

# 46. Create a small program containing several predefined numeric values. Use expressions to calculate a total, an average, a remainder, a comparison result, a logical result. Print each result with a meaningful label.
num1 = 40
num2 = 65
num3 = 78
total = num1 + num2 + num3
avg = total / 3
remainder = total % 5
print("Total :", total)
print("Avg :", avg)
print("Remainder :", remainder)
print(num1 == num2)
print(num1 == num2 and num2 == num3)

# 47. Start with a number and perform a sequence of +=, -=, *=, /=. Print the value after each operation.
num = 10
print(num)
num += 5
print(num)
num -= 5
print(num)
num *= 5
print(num)
num /= 5
print(num)

# 48. Create two different arithmetic expressions and compare their results using ==.
res1 = 10 + 5 * 2
res2 = (10 + 5) * 2
print(res1 == res2)

# 49. Create two variables referring to the same object and two variables referring to separate objects with equal contents. Use is and == to compare them.
a = 10
b = 10
c = 101
d = "101"
print(a == b)
print(a is b)
print(c == d)
print(c is d)

# 50. Store a number. Create an expression that evaluates to true when the number is not greater than 100.
num = int(input("Enter number : "))
print(not num >= 100)