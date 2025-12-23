def daily_expense(expenses):
    total = 0
    for cost in expenses:
        total += cost
    return total
breakfast = 60
lunch = 100
dinner = 150
today_expenses = [breakfast, lunch, dinner]
total = daily_expense(today_expenses)
