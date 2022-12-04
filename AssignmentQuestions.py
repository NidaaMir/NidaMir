# Q1 (String variable Name)-------------

name = 'Nida Mir'
print("\nQuestion 1")
print("Name is:", name)

# Q2 (Integer variable Year and Day)-------------

year = 2002
day = 23
print("\n\nQuestion 2")
print("Year is:", year)
print("Day is:", day)

# Q3 (Integer variable Month)--------------

month = 10
print("\n\nQuestion 4")
print("Month is:", month)

# Q4 (Data type of Name)-------------

print("\n\nQuestion 4")
print("Data type of variable 'name' is:", type(name))

# Q5 (Data type of Year)-------------

print("\n\nQuestion 5")
print("Data type of variable 'year' is:", type(year))

# Q6 (Data type of Year/Month)-------------

div1 = year / month
print("\n\nQuestion 6")
print("Data type of 'year/month' is:", type(div1))

# Q7 (Data type of Year/1)--------------

div2 = year / 1
print("\n\nQuestion 7")
print("Data type of 'year/1' is:", type(div2))

# Q8 (Data type of Year * 1)--------------

pro1 = year * 1
print("\n\nQuestion 8")
print("Data type of 'year * 1' is:", type(pro1))

# Q9 (Data type of Month + Month)---------------

add1 = month + month
print("\n\nQuestion 9")
print("Data type of 'month + month' is:", type(add1))

# Q10 (Data type of Month + Month/1)---------------

add_div = add1 / 1
print("\n\nQuestion 10")
print("Data type of 'month + month/1' is:", type(add_div))

# Q11 (Value and Data type of Name + Name)---------------

add2 = name + name
print("\n\nQuestion 11")
print("Value of 'name + name' is:", add2)
print("Data type of 'name + name' is:", type(add2))

# Q12 (Value and Data type of Name * Month)---------------

pro2 = name * month
print("\n\nQuestion 12")
print("Value of 'name * month' is:", pro2)
print("Data type of 'name * month' is:", type(pro2))

# Q13 (Value And Data type of Name * Month if Month is float)--------------

month2 = 10.0
print("\n\nQuestion 13")
print("Data type of month2 is:", type(month2))
# pro3 = name * month2
# print("\nValue of 'name * month' is:", pro3)
# print("\nData type of 'name * month' is:", type(pro3))

# NO, VALUE CANNOT BE FOUND Error in this statement (cannot multiply by float)

# Q14 (Data type of int(float(string(year))))-----------------

print("\n\nQuestion 14")
print("Data type is:", type(int(float(str(year)))))

# Q15 (Data type of float(int(string(year))))----------------

print("\n\nQuestion 15")
print("Data type is:", type(float(int(str(year)))))

# Q16 (Data  type of string(int(float(year))))---------------

print("\n\nQuestion 16")
print("Data type is:", type(str(int(float(year)))))

# Q17 (Data type of bool(Year))----------------

print("\n\nQuestion 17")
print("Data type is:", type(bool(year)))

# Q18 (Data type of bool(str(year)))-------------

print("\n\nQuestion 18")
print("Data type is:", type(bool(str(year))))


# Q19 (Data TYpe Conversions of Pi)---------------

pi = '3.14159'
float(pi)
print("\n\nQuestion 19")
print(type(pi))

# a
# int(pi)
# ValueError: invalid literal for int() with base 10: '3.14159'
print(type(pi))

# b
# str(float(int(pi)))
# ValueError: invalid literal for int() with base 10: '3.14159'
print(type(pi))

# Q20 (Creating birth date variable)--------------

slash = '/'
birthdate = str(day) + slash + str(month) + slash + str(year)
print("\n\nQuestion 20")
print("Birth date is:", birthdate)

# Q21 (Creating profile)---------------

comma = ' , '
profile = name + comma + birthdate
print("\n\nQuestion 21")
print(profile)


# Q22 (Month to bool)-------------

print("\n\nQuestion 22")
print(bool(month))

# Q23 (Name to bool)-------------

print("\n\nQuestion 23")
print(bool(name))

# Q24 (Finding False values of bool)--------------

num = 0
# zeroes are false values
print("\n\nQuestion 24")
print(bool(num))

num = 1
# any other values are true
print(bool(num))

list_1 = []
print(bool(list_1))
# empty lists, tuples etc are false

string_1 = 'Hello!'
print(bool(string_1))
# any other type of strings that have a value are true


# Q25 (Bool var)--------------

var = False
print("\n\nQuestion 25")
print("Data type of var is:", type(var))

var = 2
print(bool(var))
