import sys

n = int(input())
sentence_list = []
for i in range(n):
  my_list = sys.stdin.readline().split()
  sentence = ''
  for word in my_list[1]:
    for j in range(int(my_list[0])):
      sentence += word
  sentence_list.append(sentence)

for word in sentence_list:
  print(word)