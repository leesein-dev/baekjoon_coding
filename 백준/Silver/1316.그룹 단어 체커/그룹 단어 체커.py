import sys
import string
import re

n = int(input())
world_list = [sys.stdin.readline().strip() for i in range(n)]
group_world_count = 0
for world in world_list:
  group_world_count += 1
  for alphabet in string.ascii_lowercase:
    result = re.findall(rf'{alphabet}+', world)
    # result 길이가 2 이상이면 문자가 연속하지 않는 단어가 있다는 것을 알 수 있다.
    if len(result) >= 2:
      group_world_count -= 1
      break
      
print(group_world_count)