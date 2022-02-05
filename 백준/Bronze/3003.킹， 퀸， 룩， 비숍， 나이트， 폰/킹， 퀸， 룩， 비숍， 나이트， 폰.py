n = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
my_list = []
for i in range(len(chess)):
  my_list.append(chess[i] - n[i])
print(' '.join(map(str, my_list)))