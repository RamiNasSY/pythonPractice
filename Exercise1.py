# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

#################################

name = input("please enter your name :")
age = int(input("please enter your age :"))
year = str(100-age)
deathnot = "you will be 100 years old after : "+year
print(deathnot)
x = int(input("enter a number : "))
for i in range(x):
    print(deathnot)

