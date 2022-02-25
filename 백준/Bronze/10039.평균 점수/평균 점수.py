import sys
my_list = [int(sys.stdin.readline().strip()) for i in range(5)]
total = 0
for ele in my_list:
  if ele < 40:
    total += 40
  else:
    total += ele
print(total // 5)
