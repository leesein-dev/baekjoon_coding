n = input()
if n[-1] == '0':
  print(int(n[:-2]) + int(n[-2:]))
else:
  print(int(n[:-1]) + int(n[-1:]))