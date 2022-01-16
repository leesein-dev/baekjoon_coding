import sys

multiply = 1
for i in range(3):
  multiply *= int(sys.stdin.readline())

my_list = [0 for i in range(10)]
for num in str(multiply):
  my_list[int(num)] += 1

for element in my_list:
  print(element)