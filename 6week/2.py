def upper(a):
    count = 0
    for i in a:
        if i.isupper():
            count+=1
        
    return count

a="aBcDeFg"
ua=upper(a)
la=len(a)-ua
print(f"uppercase: {ua}")
print(f"lowercase: {la}")