import re

s = "jijJIOJIjlIijiIklm"
pattern = re.split(r"(?=[A-Z]\w*)",s)
print(pattern)

