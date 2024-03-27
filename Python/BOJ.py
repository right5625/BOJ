R = [list(input().split()) for _ in range(10)]
res = 0
for i in R:
    if len(set(i)) == 1:
        res = 1
for i in list(zip(*R)):
    if len(set(i)) == 1:
        res = 1
print(res)