import sys

n = int(input())
result_list = []
for i in range(n):
  my_list = sys.stdin.readline().split()
  for element in my_list:
    result_num = 0
    temp_num = 1
    temp_str = ''
    for ele in element:
      if ele == 'O':
        if temp_str == ele:
          temp_num += 1
        result_num += temp_num
      elif ele == 'X':
        temp_num = 1
      temp_str = ele
    result_list.append(result_num)

for num in result_list:
  print(num)