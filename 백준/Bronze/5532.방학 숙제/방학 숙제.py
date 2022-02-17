import sys
import math
my_list = [int(sys.stdin.readline().strip()) for i in range(5)]
print(my_list[0] - max([math.ceil(my_list[1] / my_list[3]), math.ceil(my_list[2] / my_list[4])]))