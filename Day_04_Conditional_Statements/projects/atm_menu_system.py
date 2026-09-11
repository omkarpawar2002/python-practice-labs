"""
Project 3 — ATM Menu System

Difficulty: Easy-Medium

Objective:
Build a basic ATM menu application.

Functional Requirements:
- Provide options: Check balance, Deposit, Withdraw, Exit
- Withdrawal should check sufficient funds

Expected Features:
- Menu selection
- Invalid choice handling
- Deposit decision
- Withdrawal validation
- Balance-related decisions

"""

print("===== ATM Menu System =====")
print()

balance = 5000

choice = int(
    input(
        "*** MENU ***"
        "\n 1.Check Balance "
        "\n 2.Deposit "
        "\n 3.Withdraw "
        "\n 4.Exit "
        "\n Enter your choice :- "
    )
)

match choice:
    case 1:
        print("Your Available Balance =", balance)
    case 2:
        deposit_amount = int(input("Enter amount you want to deposit : "))
        if deposit_amount < 0:
            print("Invalid Amount")
        else:
            balance += deposit_amount
            print("Amount Deposit Successfully")
            print("Updated Balance =", balance)
    case 3:
        withdraw_amount = int(input("Enter amount you want to withdraw : "))
        if withdraw_amount < 0:
            print("Invalid Amount")
        elif withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Amount Withdraw Successfully")
            print("Updated Balance =", balance)
        else:
            print("Insufficient Balance")
    case 4:
        print("Thank You For Using This Application")
    case _:
        print("Invalid Choice")

print()
print("===========================")
