import string

# 다이얼 리스트 만들기
def dialList():
  my_list = [[] for i in range(10)]
  i, j = 0, 3
  for index in range(10):
    if index == 0 or index == 1:
      continue
    for alphabet in string.ascii_uppercase[i:j]:
      my_list[index].append(alphabet)
    i = j
    if index == 6 or index == 8:
      j += 4
    else:
      j += 3
  return my_list

sentence = input()
dial_list = dialList()
second = 0

for ele in sentence:
  for dial in dial_list:
    if ele in dial:
      second += dial_list.index(dial) + 1

print(second)