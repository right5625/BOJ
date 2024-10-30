n = int(input())
res = inc = 0
for i in range(1, n + 1):
    inc += i
    res += inc
print(res)
