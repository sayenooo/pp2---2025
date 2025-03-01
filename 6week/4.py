import time
from math import*

a = int(input())
t = int(input())

time.sleep(t/1000)

b=sqrt(a)

print(f"Square root of {a }after {t} miliseconds is {b}")