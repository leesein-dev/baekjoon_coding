import sys

rest_num = 42
my_list = []
for i in range(10):
  num = int(sys.stdin.readline())
  try:
     my_list.index(num % rest_num)
  except ValueError:
    my_list.append(num % rest_num)

print(len(my_list))