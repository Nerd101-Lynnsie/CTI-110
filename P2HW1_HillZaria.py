###Zaria Hill - Sept. 25, 2025 - P1HW2
##Create a program that calculates and displays travel expenses

print("This program calculates and displays travel expenses")
budget = (int(input("Enter budget: ")))
print()
location = (input("Enter your travel destination: "))
print()
fuel = (int(input("How much do you think you will spend on gas? ")))
print()
accomodation = (int(input("Approximately, how much will you need for accomodation/hotel? ")))
print()
food = (int(input("Last, how much do you need for food? ")))
print()
###Travel Expenses
print("---------Travel Expenses---------")
print(f"{'Location:':<30} ${location}")
print(f"{'Initial Budget: ':<30} ${budget:.2f}")
print(f"{'Fuel: ':<30} ${fuel:.2f}")
print(f"{'Accomodation: ':<30} ${accomodation:.2f}")
print(f"{'Food: ':<30} ${food:.2f}")

print("----------------------------------")
print()
remaining = budget - fuel - accomodation - food
print(f"{'Remaining Balance: '} ${remaining:.2f}")