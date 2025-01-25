set11 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}
set11.intersection_update(set22)
set33 = set11.intersection(set22)
print(set33)
print(set11)

print(end="\n")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)