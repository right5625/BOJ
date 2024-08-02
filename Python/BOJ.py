M, N = map(int, input().split())
G = [list(map(int, input())) for _ in range(M)]
res = 0
for i in range(M):
    for j in range(N):
        diff = []
        if i > 0:
            diff.append(abs(G[i][j] - G[i - 1][j]))
        if i < M - 1:
            diff.append(abs(G[i][j] - G[i + 1][j]))
        if j > 0:
            diff.append(abs(G[i][j] - G[i][j - 1]))
        if j < N - 1:
            diff.append(abs(G[i][j] - G[i][j + 1]))
        if diff:
            res += sum(diff) / len(diff)
print(f'{res:.4f}')