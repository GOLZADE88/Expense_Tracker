
expenses = {}
expense_count = 0
total_expenses = 0

while True:
    choice = int(input('''
    Add an expense: 1
    Show expenses: 2
    Total expenses: 3
    Number of expenses: 4
    Exit: 5
    '''))

    if choice > 5 or choice < 1:
        print('Invalid request!')
        choice = int(input('''
        Add an expense: 1
        Show expenses: 2
        Total expenses: 3
        Number of expenses: 4
        Exit: 5
        '''))

    if choice == 1:
        title = input('Enter expense title: ')
        amount = int(input('Enter expense amount: '))

        total_expenses += amount
        is_new_expense = True

        if title in expenses:
            expenses[title] += amount
            is_new_expense = False

        if is_new_expense:
            expenses.update({title: amount})

    if choice == 5:
        break

    if expenses:

        if choice == 2:
            print('All expenses:', end='|')

            for key, value in expenses.items():
                print(key, value, end='|')

            print('\r')

        elif choice == 3:
            print('Total expenses =', total_expenses)

        elif choice == 4:
            print('Number of expenses:', end='|')

            for key, value in expenses.items():
                expense_count += 1
                print(key, end='|')

            print(expense_count)

        expense_count = 0

    else:
        print('No expenses recorded!')

print('You have exited!')