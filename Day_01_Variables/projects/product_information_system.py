"""
Project 3 — Product Information System

Objective:
Create a basic product information program similar to data you might find in an e-commerce application.

Functional Requirements:
Store:
- product name
- product code
- price
- stock quantity
- category
- company name
- maximum stock capacity

Expected Features:
- Meaningful variable names
- Appropriate constants
- Type inspection
- Clean formatting
- Useful comments
- Module-level documentation
"""

print("===== PRODUCT INFORMATION SYSTEM =====")
product_name = "Laptop"
product_code = "#WWERL000F1"
price = 85000.00
stock_quantity = 75
category = "Electronics"
COMPANY_NAME = "HP"
MAXIMUM_STOCK_CAPACITY = 100
print("Product Name :", product_name, type(product_name))
print("Product Code :", product_code, type(product_code))
print("Price        :", price, type(price))
print("Stock Quantity :", stock_quantity, type(stock_quantity))
print("Category     :", category, type(category))
print("Company Name :", COMPANY_NAME, type(COMPANY_NAME))
print("Maximum Stock Capacity :", MAXIMUM_STOCK_CAPACITY, type(MAXIMUM_STOCK_CAPACITY))
print("=========================================")
