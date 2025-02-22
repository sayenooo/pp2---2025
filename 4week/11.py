def square(n):
    for i in range(1,n+1):
        x=i**2
        yield x
        
n=int(input())
for i in square(n):
    print(i)
       