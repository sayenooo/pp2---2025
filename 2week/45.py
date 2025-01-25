thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #key
  print(end=" ")
  print(thisdict[x]) #value
  print(end="\n")

for x in thisdict.keys():
  print(x) #key
  print(end="\n")
for x in thisdict.values():
  print(x) #value
  print(end="\n")

for x, y in thisdict.items():
  print(x," ", y) #both

