N = int(input())
P = list(map(int, input().split()))
res = cur = 0
strick = True
for i in P:
    if i:
        cur += 1
    else:
        if strick:
            strick = False
            continue
        else:
            res = max(res, cur)
            cur = 0
    strick = True
print(max(res, cur))