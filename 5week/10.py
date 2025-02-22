import re

s = "this_Is_A_Camel_Case_String_Jerk"
matches = re.finditer(r'_([A-Z])', s)

for match in matches:
    s = s.replace(match.group(0), match.group(0).lower())

print(s)
