import json

def load_data():
    try:
        with open("budget_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"income": 0, "expenses": []}
    return data

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def add_income(data, amount):
    data["income"] += amount
    save_data(data)
    print(f"Income of ${amount} added to the budget.")

def add_expense(data, category, amount):
    data["expenses"].append({"category": category, "amount": amount})
    data["income"] -= amount
    save_data(data)
    print(f"Expense of ${amount} in the '{category}' category added to the budget.")

def calculate_budget(data):
    total_income = data["income"]
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

def expense_analysis(data):
    expense_categories = {}
    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    return expense_categories

def main():
    budget_data = load_data()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            income_amount = float(input("Enter the income amount: $"))
            add_income(budget_data, income_amount)
        elif choice == '2':
            expense_category = input("Enter the expense category: ")
            expense_amount = float(input("Enter the expense amount: $"))
            add_expense(budget_data, expense_category, expense_amount)
        elif choice == '3':
            remaining_budget = calculate_budget(budget_data)
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == '4':
            expenses_by_category = expense_analysis(budget_data)
            print("\nExpense Analysis:")
            for category, amount in expenses_by_category.items():
                print(f"'{category}': ${amount}")
        elif choice == '5':
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
