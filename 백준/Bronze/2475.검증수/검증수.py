my_list = list(map(int, input().split()))
sum_num = sum([i ** 2 for i in my_list]) % 10
print(sum_num)