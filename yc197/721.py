from datetime import datetime, timedelta

S = input()
print((datetime.strptime(S, '%Y/%m/%d') + timedelta(days = 2)).strftime('%Y/%m/%d'))
