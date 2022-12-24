class Calculator:

    def add(self):
        print(a + b)

    def sub(self):
        print(a - b)

    def mul(self):
        print(a * b)

    def div(self):
        print(a / b)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print('1 : Add, 2 : Sub, 3 : Mul, 4 : Div')
choice = int(input("Enter your choice: "))
obj = Calculator()

if choice == 1:
    print(obj.add())
elif choice == 2:
    print(obj.sub())
elif choice == 3:
    print(obj.mul())
elif choice == 4:
    print(obj.div())
else:
    print("Invalid choice")
