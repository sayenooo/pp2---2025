def is_palindrome(s):
    return s[::-1]
    
s=input()
if is_palindrome(s)==s:
    print("YES")
else:
    print("NO")