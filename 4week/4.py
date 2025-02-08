from datetime import datetime,timedelta

a=datetime.now()
x=a.replace(microsecond=0)
b=a-timedelta(days=2,hours=2,minutes=2,seconds=2)
y=b.replace(microsecond=0)

print((x-y).total_seconds())
