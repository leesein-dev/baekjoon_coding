import sys
my_list = [int(sys.stdin.readline().strip()) for i in range(2)]
result = my_list[-1] - my_list[0]
if 1 <= result and result <= 20:
  print('You are speeding and your fine is $100.')
elif 21 <= result and result <= 30:
  print('You are speeding and your fine is $270.')
elif 30 <= result:
  print('You are speeding and your fine is $500.')
else:
  print('Congratulations, you are within the speed limit!')