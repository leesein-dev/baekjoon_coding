def solve(a):
  if a <= 99:
    return True
  num_list = [int(num) for num in str(a)]
  temp = num_list[0] - num_list[1]
  for i in range(len(num_list)):
    if i != 0 and num_list[i - 1] - num_list[i] != temp:
        return False
  return True

n = int(input())
count = 0
for i in range(1, n + 1):
  if solve(i) == True:
    count += 1

print(count)