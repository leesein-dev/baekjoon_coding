n = input()
to_num = { 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15 }
result = count = 0
for i in n[::-1]:
  if i in to_num:
    i = to_num[i]
  else:
    i = int(i)
  result += (16 ** count) * i
  count += 1
print(result)