"""
=========================
Project 3 — Shopping Bill Calculator
Difficulty: Beginner-Intermediate

Objective:
Build a small expression-based shopping bill calculator.

Functional Requirements:
- Store: item price, quantity, discount information, tax information
- Calculate appropriate bill values using expressions

Expected Features:
- Subtotal calculation
- Discount calculation
- Tax calculation
- Final amount
- Comparison against a spending threshold
- Clearly organized calculations
=========================
"""

print("===== Shopping Bill Calculator =====")
print()

item_price = float(input("Enter item price : "))
quantity = int(input("Enter quantity : "))

print()

total_price = item_price * quantity
print("Total Price = ", total_price)

# For now discount is hardcoded which is 10%
discount_amt = total_price * 0.10
print("Discount Amount = ", discount_amt)

# For now tax is hardcoded which is 18%
tax = total_price * 0.18
print("Tax Added = ", tax)

final_price = total_price - discount_amt + tax
print("Final Bill = ", final_price)

print()
print("====================================")
