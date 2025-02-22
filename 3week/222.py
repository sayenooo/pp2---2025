def histogram(a,n):
    for i in range(n):
        print("*"*a[i])
        
n = int(input())
a=[]
for i in range(n):
    i=int(input())
    a.append(i)
histogram(a,n)