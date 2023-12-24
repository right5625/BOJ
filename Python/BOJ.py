N, M = map(int, input().split())
res = 0
for _ in range(N):
    if input().count('O') > M // 2:
        res += 1
print(res)