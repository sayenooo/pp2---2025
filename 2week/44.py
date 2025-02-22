thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

print(end="\n")

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1) #removes the last item

print(end="\n")

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict2["model"]
print(thisdict2)

print(end="\n")

thisdict4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict4.clear()
print(thisdict4) #will clear all items