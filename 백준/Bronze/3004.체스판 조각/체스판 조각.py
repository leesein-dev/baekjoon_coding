n = int(input())
max_count = 0
for i in range(1, n + 1):
  temp = (i + 1) * ((n - i) + 1)
  if temp > max_count:
    max_count = temp
print(max_count)