thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

print(end="\n")

thisset1 = {"apple", "banana", "cherry"}
thisset1.discard("banana")
print(thisset1)

thisset2 = {"apple", "banana", "cherry"}
x = thisset2.pop()
print(x)
print(thisset2) #removest the last item by default