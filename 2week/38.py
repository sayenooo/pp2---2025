set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
set1.difference_update(set2)
print(set3)
print(set1)

print(end="\n")

set11 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}
set33 = set11 - set22
print(set33)