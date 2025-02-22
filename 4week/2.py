import datetime

x = datetime.date.today()-datetime.timedelta(days=1)
y = datetime.date.today()
z = datetime.date.today()+datetime.timedelta(days=1)
print(x)
print(y)
print(z)