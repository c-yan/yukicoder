from datetime import datetime, timedelta

result = 0
d = datetime(2015, 1, 1)
while d < datetime(2016, 1, 1):
    if d.month == d.day // 10 + d.day % 10:
        result += 1
    d += timedelta(days=1)
print(result)
