a, b, c = map(int, input().split())
try:
  if c - b < 0:
    print(-1)
  else:
    print(a // (c - b) + 1)
except ZeroDivisionError:
  print(-1)