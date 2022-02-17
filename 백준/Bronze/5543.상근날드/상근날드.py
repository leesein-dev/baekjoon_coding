import sys
my_list = [int(sys.stdin.readline().strip()) for i in range(5)]
print(min(my_list[:3]) + min(my_list[3:]) - 50)