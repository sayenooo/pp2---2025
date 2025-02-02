def is_true(a):
    for i in range(len(a)-1):
        if a[i]==3 and a[i+1]==3:
            return True
    return False

n=int(input())
a=[]
for i in range(n):
    aa=int(input())
    a.append(aa)

if(is_true(a)):
    print("True")
else:
    print("False")