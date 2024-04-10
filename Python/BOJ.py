l, r = map(int, input().split())
res = -1
for i in range(l, r + 1):
    if len(str(i)) == len(set(str(i))):
        res = i
        break
print(res)