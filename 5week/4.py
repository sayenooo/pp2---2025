import re

s = "Hello, abbby Ajefewf ajjjjjjjjjjjAA asabAjkw Al Alan Alive Bl Blooper"

pattern = r"[A-Z][a-z]"

matches = re.findall(pattern, s)
print(matches)
