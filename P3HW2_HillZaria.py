#Zaria Hill - 10.16.2025 - P3HW2
#calculate the gross pay of an employee

#Collect info from user
employee_name = str(input("Enter employee's name: "))
num_hrs_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: $ "))

#initialize overtime variables
ot_hrs = 0
ot_pay_amount = 0

#Calculate employee regular pay and overtime data (if applicable)

if num_hrs_worked <=40:
    regular_pay = num_hrs_worked * pay_rate
    gross_pay = regular_pay

else:
    ot_hrs = num_hrs_worked - 40
    ot_payrate = pay_rate * 1.5
    ot_pay_amount = ot_hrs * ot_payrate
    regular_pay = 40 * pay_rate
    gross_pay = regular_pay + ot_pay_amount 

#Display results
print("-----------------------------------------------------")

print(f"Employee name: {employee_name}")

print(f"{'Hours Worked':<20} {'Pay Rate':<20} {'OverTime':<20} {'OverTime Pay':<20} {'RegHour Pay':<20} {'Gross Pay':<20}")
print("-----------------------------------------------------------------------------------")
print(f"{num_hrs_worked:<20} {pay_rate:<20} {ot_hrs:<20} {ot_pay_amount:<20} {regular_pay:<20} {gross_pay:<20}")