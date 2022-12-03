# \n means line change
# \t means some space
# " " means a single space
# mutable means values of elements can be changed

# MAKING A NUMBER LIST

Number_List = [2, 4, 6, 8, 10, 12]

# SLICING

print("\nMy List is:", Number_List[:])
print("\nSome elements from the list are:", Number_List[0:3:1])
print("\nElements starting from Index 2:", Number_List[2:])
print("\nList till Index 5:", Number_List[:5])
print("\nReverse order of list:", Number_List[::-1])

# MUTABILITY

Number_List[0] = 1
print("\nChanged value of Index 0 is:", Number_List[0])
print("\nCorrect order of list:", Number_List[::1])
Number_List[0:0] = 1, 2, 3
print("\nAdding in List:", Number_List[:])
print("\nEmpty List:", Number_List[1:1])
print("\nFinal List:", Number_List[:])

# ANOTHER LIST
# CONCATENATION/ADDING

Char_List = ['A', 'B', 'C', 'D', 'E', 'F']
print("\nAnother list;", Char_List)
ComboList = Number_List + Char_List
print("\nCombination of Lists is", ComboList)
print("\nLength of list is:", len(Char_List[:]))

# NESTED LIST

Names_Ages = ["Nida", "Ahmed", [20, 19]]
print("\nNames:", Names_Ages[0], "and", Names_Ages[1])
print("\nAges:", Names_Ages[2][0], "and", Names_Ages[2][1])
print("\nCapital Letters of Names:", Names_Ages[0][0], "and", Names_Ages[1][0])
print("\nReverse Order:", Names_Ages[::-1])
print("\nReverse Order of Nested List:", Names_Ages[2][::-1])
print("\nLength of list is:", len(Names_Ages[:]))

# TYPE FUNCTION

print("\nData type of Number List is:", type(Number_List))
print("Data type of Char List is:", type(Char_List))
print("Data type of Names and Ages List is:", type(Names_Ages))

# REPETITION OPERATOR

print("\nRepeat three times:", Names_Ages * 3)

# INT LIST

Number2_List = [3, 5, 6, 8, 14, 20]

# COMPARISON OPERATOR

print(Number_List > Number2_List)
print(Number_List[0] < Number_List[0])
print(Number_List[2] == Number_List[5])
print(Number_List[2] != Number_List[5])


# CHECKING PRESENCE

print("Nida" in Names_Ages)
print("21" in Number_List)
print('C' in Char_List)
print(2 not in Char_List)

# INSERTING ELEMENT AT THE END OF LIST

print(Number_List)
Number_List.append(13)
print(Number_List)

# FOR MULTIPLE ELEMENTS USE LOOP

for i in range(14, 21):
    Number_List.append(i)
print(Number_List)

# OR USE EXTEND()

Number_List.extend([21, 22, 23, 24, 25])
print(Number_List)

# INSERT A VALUE IN THE MIDDLE OF LIST

Number_List.insert(3, 4)
print(Number_List)
Number_List.insert(5, 5)
print(Number_List)
Number_List.insert(8, 7)
print(Number_List)
Number_List.insert(10, 9)
print(Number_List)

# REMOVE ELEMENTS

Number_List.remove(4)
print(Number_List)

# POP REMOVES LAST ELEMENT

Number_List.pop()
print(Number_List)

# REVERSE LIST

Number_List.reverse()
print(Number_List)

# MIN AND MAX

print(min(Number_List))
print(max(Number_List))

# LENGTH OPERATOR

print("\nLength of list is:", len(Number_List[:]))

# COUNT

print(Number_List.count(1))
print(Number_List.count(4))

# SORT

Number_List.sort()
print(Number_List)

# CLEAR

Number_List.clear()
print(Number_List)

