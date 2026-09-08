"""
=========================
Project 4 — Product Billing Generator

Objective:
Create a simple product billing program.

Functional Requirements:
- Collect: product name, quantity, price
- Calculate the total purchase amount
- Display a basic bill containing: product, quantity, unit price, total amount

Expected Features:
- Interactive user input
- Correct numeric conversion
- Decimal prices
- Clear bill layout
- Correct total calculation
=========================
"""

print("===== Product Billing Generator =====")
print()

# Here We Get Product Details
product_name = input("Enter product here : ")
quantity = int(input("Enter quantity : "))
price = float(input("Enter product price : "))

# Total Amount
total_amt = price * quantity
print()

print("Product      :", product_name)
print("Quantity     :", quantity)
print("Unit Price   :", price)
print("Total Amount :", total_amt)


print()
print("=====================================")
