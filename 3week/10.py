def unique(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

a = []
while True:
    i = int(input())
    a.append(i)
    if i==0:
        break

print(unique(a))