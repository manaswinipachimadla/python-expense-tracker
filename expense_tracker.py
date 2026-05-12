import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    try:
        with open(FILE_NAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No expenses found.\n")


def total_expenses():
    total = 0

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                total += float(row['Amount'])

        print(f"\nTotal Expenses: ₹{total}\n")

    except FileNotFoundError:
        print("No expense data found.\n")


def menu():
    initialize_file()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            total_expenses()

        elif choice == '4':
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Try again.\n")


menu()
