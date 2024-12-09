# Define a list to store expenses
expenses = []

def add_expense(date, category, amount, description):
    """
    Add a new expense to the expenses list.
    """
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully.")

def remove_expense(index):
    """
    Remove an expense from the expenses list by index.
    """
    if index < 0 or index >= len(expenses):
        print("Invalid index. No expense removed.")
        return
    expenses.pop(index)
    print("Expense removed successfully.")

def show_expenses():
    """
    Display the list of expenses in a formatted table.
    """
    if not expenses:
        print("No expenses recorded.")
        return

    print("Your Expenses:")
    print("Index | Date       | Category     | Amount   | Description")
    print("-------------------------------------------------------")

    for idx, expense in enumerate(expenses, start=1):
        date = expense.get('date', 'N/A')
        category = expense.get('category', 'N/A')
        amount = expense.get('amount', 'N/A')
        description = expense.get('description', 'N/A')
        expense_details = f"{idx}. {date} | {category} | {amount} | {description}"
        print(expense_details)

def main():
    """
    Main function to interact with the expense manager.
    """
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Show Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            add_expense(date, category, amount, description)

        elif choice == "2":
            show_expenses()
            index = int(input("Enter the index of the expense to remove: ")) - 1
            remove_expense(index)

        elif choice == "3":
            show_expenses()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
