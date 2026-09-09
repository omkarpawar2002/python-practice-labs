"""
=========================
Project 4 — User Access Eligibility Checker
Difficulty: Intermediate

Objective:
Build a program that determines whether a user should receive access to a fictional system.

Functional Requirements:
- Evaluate information such as: age, role, account status, permission, whether a required value is None
- Combine these conditions to determine eligibility

Expected Features:
- Age-range validation
- Allowed-role membership checking
- Permission checking
- Multiple logical conditions
- None identity checking
- Safe short-circuit expressions

"""

print("===== User Access Eligibility Checker =====")

age = int(input("Enter your age : "))
role = input("Enter your role : ")
account_status_active = True
permission_allowed = True

roles = ["admin", "employee", "manager"]

# Individual checks
age_validation = 18 <= age <= 60
role_allowed = role in roles
account_ok = account_status_active
permission_ok = permission_allowed

eligible = age_validation and role_allowed and account_ok and permission_ok

print("Valid Age          : ", age_validation)
print("Allowed Role       : ", role_allowed)
print("Account Active     : ", account_ok)
print("Permission Allowed : ", permission_ok)

print("============================================")
print("Final Eligibility  : ", eligible)
print("============================================")