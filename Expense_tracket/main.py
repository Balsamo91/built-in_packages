"""
Example using csv, os, datetime: Expen tracker
This script uses the csv, os, and datetime modules to implete a simple expense trackr.
It allows the user to add expenses, which are then saved to a csv file with a timestamp.
"""

import csv
import os
from datetime import datetime

def add_expense(amount, category):
    filename = "expenses.csv"
    # check if the file exist to write headers
    file_exist = os.path.isfile(filename)
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ['Date', 'Amount', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exist:
            writer.writeheader() # Write header only once

        now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        writer.writerow({'Date': now, 'Amount': amount, 'Category': category})

    print(f"Added expense {amount} in category '{category}' on {now}")



while True:
    print("Expense Tracker")
    print("1. Add expense")
    print("2. exit")

    choice = input(":Enter your choice: ")

    if choice == "1":
        amount = float(input("enter expense amount: "))
        category = input("Enter expense category: ")
        add_expense(amount, category)
        pass
    elif choice == "2":
        print("Exiting program")
        break
    else:
        print("Invalid choice, try again!")