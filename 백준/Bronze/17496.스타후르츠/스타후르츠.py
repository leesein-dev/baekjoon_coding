n, t, c, p = map(int, input().split())
result = 0
for i in range(1, n, t):
  if i + t > n:
    break
  result += p * c
print(result)