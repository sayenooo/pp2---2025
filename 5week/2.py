import re

s = "He1llo, abbby nabb0me is abbbZhansaya 0abbb ab as0 asabababljkn abbbb abb"
pattern = r"ab{2,3}\b"
ss = re.findall(pattern,s)
print(ss)