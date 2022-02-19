import sys
n = int(input())
my_list = [float(sys.stdin.readline().strip()) * 0.8 for i in range(n)]
for i in my_list:
  print('$%0.2f' % i)