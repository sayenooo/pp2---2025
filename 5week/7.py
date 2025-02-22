import re

s = "this_is_a_snake_case_string"
matches = re.finditer(r'_([a-z])', s)

for match in matches:
    s = s.replace(match.group(0), match.group(0).upper())

print(s)
