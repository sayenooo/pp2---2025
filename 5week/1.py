import re

s = "her weh fw uwihuw ab ab abb aabd abb diuqh"
pattern = r"ab*" 
a = re.findall(pattern,s)

print(a)