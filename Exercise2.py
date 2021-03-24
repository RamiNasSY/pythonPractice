# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#######################
num = int(input("please enter any number : "))
check = int(input("give me number : "))
answer = num % 2
multiple = num % 4
if multiple == 0:
    print("the number is multiple of 4")
elif answer == 0:
    print("the number is even")
else:
    print("the number is odd")
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
