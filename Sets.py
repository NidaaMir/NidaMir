# MAKING SETS

Set1 = {1, 2, 3, 4, 5, 6}
Set2 = {7, 8, 9, 10}

# CHECKING TYPE

print("Data type is:", type(Set2))

# ADDITION

Set2.add(11)
print("\nAfter addition set is:", Set2)

Set1.add(7)
print("\nAfter addition set is:", Set1)

# DIFFERENCE

print("\nDifference between set is:", Set2 - Set1)

# UPDATE

Addition = {12, 13, 14, 15}
Set2.update(Addition)
print("\nUpdated set is:", Set2)

# UNION

print("\nUnion is:", Set1.union(Set2))

# INTERSECTION

print("\nIntersection is:", Set1.intersection(Set2))

# SYSTEMATIC DIFFERENCE

print("\nSystematic Difference is :", Set2.difference(Set1))

# REMOVE AND DISCARD

Set2.discard(7)
print("\nSet without 7 is:", Set2)
Set1.remove(7)
print("\nSet without 7 is:", Set1)

# CLEAR and DELETE

Set3 = {1, 2, 3}
Set3.clear()
print("\n", Set3)

# POP

Set2.pop()
print("\nPopped first element:", Set2)

# MAX and MIN

print("\nMax of Set1", max(Set1))
print("\nMin of Set2:", min(Set2))

# SORTED

print("\nSorted Set is:", sorted(Set2))

