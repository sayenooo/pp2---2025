def string_permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i in range(len(s)):
        char = s[i]
        rest = s[:i] + s[i+1:]
        for perm in string_permutations(rest):
            result.append(char + perm)
    return result


perms = string_permutations(input())
for perm in perms:
    print(perm)
