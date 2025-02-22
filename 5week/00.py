import re
import csv

# Читаем файл безопасно
with open("5week/row.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Ищем БИН
BINpattern = r"\nБИН\s(?P<BIN>\d+)"
BINmatch = re.search(BINpattern, text)
BINresult = BINmatch.group("BIN") if BINmatch else "Not found"
print("БИН:", BINresult)

# Ищем номер чека
Checkpattern = r"\nЧек\s(?P<Check>№\d+)"
Checkmatch = re.search(Checkpattern, text)
Checkresult = Checkmatch.group("Check") if Checkmatch else "Not found"
print("Чек:", Checkresult)

# Ищем номер заказа
Orderpattern = r"\n.+\s(?P<Order>№\d+)"
Ordermatch = re.search(Orderpattern, text)
Orderresult = Ordermatch.group("Order") if Ordermatch else "Not found"
print("Заказ:", Orderresult)

# Ищем фискальный чек
FCheckpattern = r"\nФИСКАЛЬНЫЙ ЧЕК\n(?P<FCheck>\w+)\n(?P<FCheck1>\w+)\n(?P<FCheck2>\w+)\n(?P<FCheck3>\w+)\n(?P<FCheck4>\w+)"
FCheckresult = re.compile(FCheckpattern)
fciteration = FCheckresult.finditer(text)

print("Фискальный чек:")
for match in fciteration:
    print(match.group("FCheck"), match.group("FCheck1"), match.group("FCheck2"), match.group("FCheck3"), match.group("FCheck4"))

print("\n📌 Создаём таблицу...")

# Исправленный паттерн для товаров (исключает пустые строки)
ItemPattern = r"(?P<ItemRowNumber>\S+)\s*\n\s*(?P<ItemName>.+)\s*\n\s*(?P<ItemPrice1>\d+[\.,]?\d*)\s*\n\s*(?P<ItemPrice2>\d+[\.,]?\d*)\s*\n\s*(?P<ItemTotalPrice>\d+[\.,]?\d*)"
prog = re.compile(ItemPattern)
Itemiterator = prog.finditer(text)

# Записываем в CSV с разделителем ";"
with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")  
    writer.writerow(["ItemRowNumber", "ItemName", "ItemPrice1", "ItemPrice2", "ItemTotalPrice"])
    
    found_items = False  # Проверим, есть ли данные
    for ItemResult in Itemiterator:
        writer.writerow([
            ItemResult.group("ItemRowNumber"),
            ItemResult.group("ItemName"),

            ItemResult.group("ItemPrice1"),
            ItemResult.group("ItemPrice2"),
            ItemResult.group("ItemTotalPrice")
        ])
        found_items = True  # Найден хотя бы один товар

    if not found_items:
        print("❌ Ошибка: Не найдено ни одного товара!")

print("✅ Таблица создана: data.csv")

