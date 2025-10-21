#Zaria Hill
#Learn about "for loops"
'''
#Use the range funtion to loop a certain number of times
#the ending value (the last number = 5 so line 8 will print numbers 1-4) for range is not inclusive

for item in range(1,11):
    print("😝🐢🦦")
    print(f"The value of item is: {item}")
    print()
'''

'''
#To count by 2's start the range at zero and and a third value of 2
for item in range(0,11,2):
    print("😝🐢🦦")
    print(f"The value of item is: {item}")
    print()
'''

'''
#Use the for loop to loop through a list
colors = ["red", "lavender", "sage green", "yellow"]

for color in colors:
    print(f"The current color is: {color}")
'''

'''
#Add friend Names into list using a loop
friends = []

for friend in range(3):
    friend_name = input("Enter a friends name: ")
    friends.append(friend_name)
#Loop breaks here
print(friends)
'''