thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #key
  print(thisdict[x]) #value

for x in thisdict.keys():
  print(x) #key
for x in thisdict.values():
  print(x) #value


for x, y in thisdict.items():
  print(x, y) #both

