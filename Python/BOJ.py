from collections import defaultdict

res = defaultdict(int)
N, M = map(int, input().split())
for i in range(1, N + 1):
    for j in range(1, M + 1):
        res[i + j] += 1
print(*[k for k, v in res.items() if v == max(list(res.values()))], sep = '\n')