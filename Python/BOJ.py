N = int(input())
res = 0
for i, j in zip(input(), input()):
    if i == 'C' and i == j:
        res += 1
print(res)