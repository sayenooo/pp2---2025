import re

s = "Hello, abbb Ajefewf ajjjjjjjjjjjAAab asabAjkw Al Alan Alive Bl Blooper"

pattern = r"\ba\w*b\b"

matches = re.findall(pattern, s)
print(matches)
