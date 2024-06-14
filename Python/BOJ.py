x = int(input())
m = int(input())
res = 'No such integer exists.'
for n in range(1, m):
    if (x * n) % m == 1:
        res = n
        break
print(res)