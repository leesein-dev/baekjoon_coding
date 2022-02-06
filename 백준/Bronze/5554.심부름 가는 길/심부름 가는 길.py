import sys
total = sum([int(sys.stdin.readline()) for i in range(4)])
print(total // 60, total % 60, sep='\n')