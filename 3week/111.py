def is_palindrom(s):
    return s[::-1]
    
s=input()
if is_palindrom(s)==s:
    print("YES")
else:
    print("NO")