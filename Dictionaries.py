# MAKING A DICTIONARY

STUDENTS = {'Name1': 'Nida', 'Age1': 20, 'Gender1': 'F', 'Name2': 'Musfira', 'Age2': 21, 'Gender2': 'F'}
print("\nDictionary is:", STUDENTS)

print("\nThe Keys are:", STUDENTS.keys())
print("\nThe values are:", STUDENTS.values())
print("\nName 1 is:", STUDENTS['Name1'])

STUDENTS['Name3'] = 'Mehran'
STUDENTS['Age3'] = '18'
STUDENTS['Gender3'] = 'M'
print("\nModified Dictionary is:", STUDENTS)

STUDENTS.update({'Name4': 'Laiba', 'Age4': 19, 'Gender4': 'F'})
print(STUDENTS)

STUDENTS.pop('Name4')
print(STUDENTS)
del STUDENTS['Age4']
del STUDENTS['Gender4']
print(STUDENTS)

SPAM = {20: 20, 40: 40}
SPAM.clear()
print(SPAM)

STUDENTS.popitem()
print(STUDENTS)

del SPAM

print(len(STUDENTS))
print(sorted(STUDENTS))
print(STUDENTS.copy())

print(STUDENTS.get('Age5'))
print(type(STUDENTS))
print(type(STUDENTS['Name1']))

SPAM2 = {20: 20, 40: 40, 60: 60}
SPAM3 = {80: 80, 100: 100, 120: 120}
SPAM4 = SPAM2.copy()
SPAM4.update(SPAM3)
print(SPAM4)

NUM_SQUARES = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print(NUM_SQUARES)



