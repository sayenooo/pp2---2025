fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print(end="\n")

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits if "a" in x]

print(newlist1)