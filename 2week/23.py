list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print(end="\n")

list01 = ["a", "b" , "c"]
list02 = [1, 2, 3]

for x in list02:
  list01.append(x)

print(list01)

print(end="\n")

list11 = ["a", "b" , "c"]
list22 = [1, 2, 3]

list11.extend(list22)
print(list11)