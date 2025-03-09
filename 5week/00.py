import re

f = open("row.txt")
text = f.read()

ProductName = r"\n\b\d*.\n(?P<pname>\w*)"
ProductNameResult = re.search(ProductName).group