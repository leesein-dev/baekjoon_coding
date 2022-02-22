import datetime
d, h, m = map(int, input().split())
time_1 = datetime.timedelta(days=11, hours=11, minutes=11)
time_2 = datetime.timedelta(days=d, hours=h, minutes=m)
result = int((time_2 - time_1).total_seconds() / 60)
if result < 0:
  print(-1)
else:
  print(result)