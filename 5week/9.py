import re

s = "ijijJIOJIjlIijiIklm"

pattern = r"([A-Z])"
replacement = r" \1"

ss = re.sub(pattern, replacement, s)
print(ss)
