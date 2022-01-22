from string import ascii_lowercase

word = input()
my_list = []

for i in ascii_lowercase:
  if i in word:
    my_list.append(str(word.index(i)))
  else:
    my_list.append('-1')

print(' '.join(my_list))
