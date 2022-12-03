# MAKING A TUPLE

NumTup1 = (4, 6, 8, 9, 2, 0)
print(NumTup1)
print(NumTup1[4])

# USE CONCATENATION FOR ADDING ELEMENTS

NumTup2 = (3, 6, 8, 9, 0, 1)
NumTup3 = NumTup1 + NumTup2
print(NumTup3)

# DIFFERENT FUNCTIONS

print(len(NumTup3))
print(type(NumTup3))

print(3 in NumTup3)
print(5 not in NumTup3)
print(NumTup3.count(2))


print(min(NumTup3))
print(max(NumTup3))

NumTup4 = (2, 6, 8, 10, (3, 6, 9))
print(NumTup4[0])
print(NumTup4[4])

print(NumTup4[::-1])

print(NumTup3 * 3)

del NumTup2

print(sorted(NumTup3))

print(sum(NumTup3))

NumTup5 = (1, 2, 1, 2, 3, 3)
print(NumTup5)

print(sorted(NumTup5))

NumList1 = [1, 2, 1, 2, 3, 3]
NumList1.sort()
print(NumList1)

NumSet1 = {1, 2, 1, 2, 3, 3}
print(NumSet1)
