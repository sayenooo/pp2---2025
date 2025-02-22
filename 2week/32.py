thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

print(end="\n")

thisset1 = {"apple", "banana", "cherry"}
thisset1.discard("banana")
print(thisset1)

print(end="\n")

thisset2 = {"apple", "banana", "cherry"}
x = thisset2.pop()
print(x)
print(thisset2) #removest the last item by default

print(end="\n")

thisset3 = {"apple", "banana", "cherry"}
thisset3.clear()
print(thisset3) #will clear the set

print(end="\n")

thisset4 = {"apple", "banana", "cherry"}
del thisset4
print(thisset4) #will delete the set completely
