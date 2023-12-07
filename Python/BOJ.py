N = int(input())
DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    DP[i][0] = 1
    DP[i][i] = 1
    DP[i][1] = i
for i in range(3, N + 1):
    for j in range(2, i):
        DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j]
print(DP[N][5])