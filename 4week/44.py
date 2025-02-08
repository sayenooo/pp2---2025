def squares(n,m):
    for i in range(n,m+1):
        yield i**2
        
n,m=map(int,input().split())
for i in squares(n,m):
    print(i)