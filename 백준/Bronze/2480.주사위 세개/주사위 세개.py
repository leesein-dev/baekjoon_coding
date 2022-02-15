my_list = list(map(int, input().split()))
my_list.sort(reverse = True)
if my_list[0] == my_list[-1]:
  print(10000 + my_list[0] * 1000)
elif my_list[0] != my_list[1] and my_list[1] != my_list[-1]:
  print(my_list[0] * 100)
else:
  print(1000 + my_list[1] * 100)