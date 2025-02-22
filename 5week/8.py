import re

s = "ijijJIOJIjlIijiIklm"
pattern = re.split(r"(?=[A-Z]\w*)",s)
print(pattern)

