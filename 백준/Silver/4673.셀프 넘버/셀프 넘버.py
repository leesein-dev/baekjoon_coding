def notSelfNumberList(a):
  self_num_list = []
  i = 1
  while True:
    temp = i
    for num in str(temp):
      temp += int(num)
    if i > a:
      break
    self_num_list.append(temp)
    i += 1
  return self_num_list

n = 10000
my_list = notSelfNumberList(n)
self_number_list = [i for i in range(1, n + 1) if i not in my_list]
for num in self_number_list:
  print(num)