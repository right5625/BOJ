import sys

input = lambda: sys.stdin.readline().rstrip()

dic = {i: 0 for i in range(1, 51)}
n = int(input())
for _ in range(n):
    for __ in range(10):
        for j in list(map(int, input().split())):
            dic[j] += 1
res = []
for k, v in dic.items():
    if v > n * 2:
        res.append(k)
print(*res) if res else print(-1)
