a, b = map(int, input().split())
my_list = [i - (a * b) for i in list(map(int, input().split()))]
print(' '.join(map(str, my_list)))