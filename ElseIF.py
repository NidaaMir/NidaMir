#A=45
#B=67
#C=88
#if (B>A):
#    print(B)
#else:
#    print(A)
A= int(input("Enter a Number"))
B= int(input("Enter a number"))
C= int(input("Enter a number"))

if (A>B) & (A>C):
    print("A is greater")
elif (B>A) & (B>C):
    print("B is greater")
else:print("C")