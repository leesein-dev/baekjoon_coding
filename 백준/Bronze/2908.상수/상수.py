n = input().split()
new_n = [int(num[::-1]) for num in n]
print(max(new_n))