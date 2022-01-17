import sys

count = int(input())
score_list = list(map(int, sys.stdin.readline().split()))
max_score = max(score_list)
new_avarage = 0
for num in score_list:
  new_avarage += num / max_score * 100
print(new_avarage / count)