N, A, B = map(int, input().split())
res1, res2 = 1, 1
for _ in range(N):
    res1 += A
    res2 += B
    if res1 < res2:
        res1, res2 = res2, res1
    elif res1 == res2:
        res2 -= 1
print(res1, res2)
