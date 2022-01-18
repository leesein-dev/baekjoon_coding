import sys

n = int(input())
my_list = []
for i in range(n):
  my_list.append(list(map(int, sys.stdin.readline().split())))
  
for list in my_list:
  count = list[0]
  avarage_score = sum(list[1:]) / count
  up_score_count = 0
  for num in list[1:]:
    if avarage_score < num:
      up_score_count += 1
  print("%.3f%%" % round(up_score_count / count * 100.0, 3))