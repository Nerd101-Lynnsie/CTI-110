#Zaria Hill - Oct. 2,2025 - P2HW2
#Create a program that will display the lowest & highest grades +  calculate the sum and average of all the values

#Prompt the user to enter a grade for Modules 1 - 6
module1 = float(input("Enter grade for Moddule 1: "))
module2 = float(input("Enter grade for Moddule 2: "))
module3 = float(input("Enter grade for Moddule 3: "))
module4 = float(input("Enter grade for Moddule 4: "))
module5 = float(input("Enter grade for Moddule 5: "))
module6 = float(input("Enter grade for Moddule 6: "))

#display the lowest & highest grades +  calculate the sum and average using values from the list
print()
print("---------- Results----------")
grades = [module1, module2, module3, module4, module5, module6]

#display lowest grade
lowest_grade = min(grades)
print(f"{'Lowest Grade:':<20} {lowest_grade:.1f}")

#display highest grade
highest_grade = max(grades)
print(f"{'Highest Grade:':<20} {highest_grade:.1f}")

#calculate and display sum of grades
sum_grades = sum(grades)
print(f"{'Sum of Grades:':<20} {sum_grades:.1f}")

#calculate and display average of grades
average = sum(grades) / len(grades)
print(f"{'Average:':<20} {average:.2f}")