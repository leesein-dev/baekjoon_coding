import math
a, b = map(int, input().split())
t1, t2 = math.ceil((a + b) / 2), math.ceil(a - ((a + b) / 2))
if a > b and t1 + t2 == a:
  print('%d %d' % (t1, t2))
elif a == 0 and b == 0:
  print('%d %d' % (t1, t2))
else:
  print(-1)