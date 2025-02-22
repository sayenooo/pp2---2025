from math import*
n,l=map(int,input().split())
s=round((l**2*n)//4*tan(pi/n))

print(f"Input number of sides: {n}")
print(f"Input the length of a side: {l}")
print(f"The area of the polygon is: {s}")