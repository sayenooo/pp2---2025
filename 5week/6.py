import re

s = "Hello, abbb Ajefew.f ajjjjjjjj.jjjAAab asabAjkw Al Alan Alive Bl Blooper"

pattern=r"[. ,]"
matches = re.sub(pattern, ":", s)
print(matches)
