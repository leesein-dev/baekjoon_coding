import re

n = input()
result = re.sub(r'(c=|c-|dz=|d-|lj|nj|s=|z=)', '*', n)
print(len(result))