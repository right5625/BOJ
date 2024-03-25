prev = res = ''
for i in input():
    if prev != i:
        res += i
    prev = i
print(res)