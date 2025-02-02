def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a = []
while True:
    i = int(input())
    a.append(i)
    if i==0:
        break
    
b = []
for i in a:
    if is_prime(i):
        b.append(i)
        
print(b, end = " ")