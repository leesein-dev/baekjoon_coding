import sys
my_list = [sys.stdin.readline().strip() for i in range(2)]
s = sum(list(map(int, my_list[0].split())))
t = sum(list(map(int, my_list[1].split())))
print(max([s, t]))