print("My Budget for a Semester!")
# Budget, Food, Electricity, Rent, Miscellaneous
# All Figures Monthly
# Semester will be 4 months long
# Budget is per month
budget_per_month = 800
months_per_semester = 4
budget_per_semester  = budget_per_month * months_per_semester
meal_expense_per_day = 12
day_per_week = 7
weeks_per_month = 4
food_expense_per_semester = meal_expense_per_day * day_per_week * weeks_per_month * months_per_semester
electricity_per_week = 6
electricity_expense_per_semester = electricity_per_week * weeks_per_month * months_per_semester
rent_per_month = 310
rent_per_semester = rent_per_month * months_per_semester
miscellaneous_per_month = 100
miscellaneous_per_semester = miscellaneous_per_month * months_per_semester
total_expense_per_semester = food_expense_per_semester + electricity_expense_per_semester + rent_per_semester + miscellaneous_per_semester
print(f"My available budget per semester is €{budget_per_semester}")
print(f"My expenditures for this semester is €{total_expense_per_semester}")
print(f"This leaves me with €{budget_per_semester - total_expense_per_semester} to spend this semester")