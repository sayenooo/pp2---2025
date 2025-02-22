import re
import csv

f = open("5week/row.txt","r",encoding="utf-8")
text = f.read()

BINpattern = r"\nБИН\s(?P<BIN>[0-9]+)"
BINresult = re.search(BINpattern, text).group("BIN")
print(BINresult)

Checkpattern = r"\nЧек\s(?P<Check>№\d+)"
Checkresult = re.search(Checkpattern, text).group("Check")
print(Checkresult)

Orderpattern = r"\n.+\s(?P<Order>№\d+)"
Orderresult = re.search(Orderpattern, text).group("Order")
print(Orderresult)

FCheckpattern = r"\nФИСКАЛЬНЫЙ ЧЕК\n(?P<FCheck>\w+)\n(?P<FCheck1>\w+)\n(?P<FCheck2>\w+)\n(?P<FCheck3>\w+)\n(?P<FCheck4>\w+)"
FCheckresult = re.compile(FCheckpattern)
fciteration = FCheckresult.finditer(text)

for FCheckpattern in fciteration:
    print(FCheckpattern.group("FCheck"),FCheckpattern.group("FCheck1"),FCheckpattern.group("FCheck2"),FCheckpattern.group("FCheck3"),FCheckpattern.group("FCheck4"))

print("creating a table")

ItemPattern = r"(?P<ItemRowNumber>.*)\n(?P<ItemName>.*)\n(?P<ItemPrice1>.*)\sx\s(?P<ItemPrice2>.*)\n(?P<ItemTotalPrice>.*)"

prog = re.compile(ItemPattern)
Itemiterator = prog.finditer(text)

with open("data.csv","w",newline="",encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ItemRowNumber","ItemName","ItemPrice1","ItemPrice2","ItemTotalPrice"])
    for ItemResult in Itemiterator:
        writer.writerow([ItemResult.group("ItemRowNumber"),ItemResult.group("ItemName"),ItemResult.group("ItemPrice1"),ItemResult.group("ItemPrice2"),ItemResult.group("ItemTotalPrice")])