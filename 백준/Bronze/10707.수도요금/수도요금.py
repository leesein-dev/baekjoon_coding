import sys
my_list = [int(sys.stdin.readline().strip()) for i in range(5)]
x_price = my_list[0] * my_list[-1]
y_price = my_list[1]
if my_list[-1] > my_list[2]:
  y_price += (my_list[-1] - my_list[2]) * my_list[3]
print(min([x_price, y_price]))