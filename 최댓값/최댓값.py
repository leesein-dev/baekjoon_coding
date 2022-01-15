import sys

data = []
for i in range(10):
  data.append(list(map(int, sys.stdin.readline().split())))
max_num = max(data)
print(max_num[0], data.index(max_num) + 1, sep="\n")