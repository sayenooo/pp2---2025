def numbers(n):
    for i in range(n,0,-1):
        yield i
        
n=int(input())
for i in numbers(n):
    print(i)