import sys

n, x = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
new_list = []

for i in range(len(sequence)):
  if sequence[i] < x:
    new_list.append(str(sequence[i]))

print(' '.join(new_list))