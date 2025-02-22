def reversed(s):
    word = s.split()
    new = []
    for i in range(len(word)-1,-1,-1):
        new.append(word[i])
    return " ".join(new)
s=input()
print(reversed(s))

            
    