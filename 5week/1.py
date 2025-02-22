import re

s = "He1llo, abmy na0me is Zhansaya 0a ab as0 asljkn"
pattern = r"a*b*"
ss = re.findall(pattern,s)
print(ss)