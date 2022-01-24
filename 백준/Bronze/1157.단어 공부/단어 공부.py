word = input().upper()
my_dict = {}

for i in word:
  if i in my_dict.keys():
    my_dict[i] += 1
    continue
  my_dict[i] = 1

max_count = max(my_dict.values())
same_word_list = [ key for key in my_dict if my_dict[key] == max_count ]

if len(same_word_list) > 1:
  print('?')
else:
  print(same_word_list[0])