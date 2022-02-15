h, m = map(int, input().split())
m += int(input())
h += m // 60
m %= 60
if h > 23:
  h -= 24
print(h, m)