def upper(a):
    count = 0
    for i in a:
        if i.isupper():
            count = 1
    return count

a="aBcDeFg"
count = 0
ua=filter(upper,a)
for i in ua:
    count += 1
la=len(a)-count
uaa = count
print(f"uppercase: {uaa}")
print(f"lowercase: {la}")