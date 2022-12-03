def statement():
    print("\nHello! Welcome :)\n")


def info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("\nYour info is: ", name, age)


statement()
info()


def year(current_year, age):
    birth_year = current_year - age
    return birth_year


output = year(2022, 20)
print("\nYour birth year is:", output)

