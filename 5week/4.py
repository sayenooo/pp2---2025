import re

s = "Hello, abbby Ajefewf ajjjjjjjjjjjAA asabAjkw Al Alan Alive Bl Blooper"

pattern = r"\b[A-Z]\w*"

matches = re.findall(pattern, s)
print(matches)
