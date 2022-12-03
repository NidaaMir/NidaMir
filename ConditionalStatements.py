# python program to illustrate If statement

i = 10
if i > 15:
    print("10 is less than 15")
print("I am not in IF")

# python program to illustrate If else statement

i = 20
if i < 15:
    print("i is smaller than 15")
    print("I'm in IF Block")
else:
    print("i is greater than 15")
    print("I'm in ELSE Block")
print("I'm not in IF and not in ELSE Block")

# python program to illustrate nested If statement
i = 10
if i == 10:
    #  First if statement
    if i < 15:
        print("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

# A school has the following rules for Grading System:

# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A

# Ask user to enter Marks and print the corresponding Grade.

marks = int(input("Enter Your Marks:"))
if marks < 25:
    print("F")
elif 25 <= marks < 45:
    print("E")
elif 45 <= marks < 50:
    print("D")
elif 50 <= marks < 60:
    print("C")
elif 60 <= marks < 80:
    print("B")
else:
    print("A")

# Take values of length and breadth of a rectangle from user and check if it is square or not.

print("Enter length of rectangle")
length = input()
print("Enter breadth of rectangle")
breadth = input()
if length == breadth:
    print("Yes, it is a square")
else:
    print("No, it is a Rectangle")
