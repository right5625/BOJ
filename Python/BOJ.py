n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]
for _ in range(int(input())):
    i, d = map(int, input().split())
    res = 0
    for j in range(1, n + 1):
        if ((P[i - 1][0] - P[j - 1][0]) ** 2 + (P[i - 1][1] - P[j - 1][1]) ** 2) ** 0.5 <= d:
            res += 1
    print(res - 1)