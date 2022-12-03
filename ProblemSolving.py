# finding out number of vowels

string = input("Enter a word!")
count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for s in string:
    if s in vowels:
        count = count + 1

print("There are this many vowels:", count)

