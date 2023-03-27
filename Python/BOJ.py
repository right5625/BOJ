import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

M, N, H = map(int, input().split())
T = [[[-1 for __ in range(M + 2)] for _ in range(N + 2)]] + [[[-1 for __ in range(M + 2)]] + [[-1] + list(map(int, input().split())) + [-1] for __ in range(N)] + [[-1 for __ in range(M + 2)]] for _ in range(H)] + [[[-1 for __ in range(M + 2)] for _ in range(N + 2)]]
q = deque([[(i, j, k) for i in range(1, H + 1) for j in range(1, N + 1) for k in range(1, M + 1) if T[i][j][k] == 1]])
mx = [-1, 1, 0, 0, 0, 0]
my = [0, 0, -1, 1, 0, 0]
mz = [0, 0, 0, 0, -1, 1]
res = 0
while q:
    v = q.popleft()
    l = []
    for i in v:
        for j in range(6):
            x = i[2] + mx[j]
            y = i[1] + my[j]
            z = i[0] + mz[j]
            if T[z][y][x] == 0:
                T[z][y][x] = 1
                l.append((z, y, x))
    if l:
        q.append(l)
        res += 1
flag = False
for i in range(1, H + 1):
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            if T[i][j][k] == 0:
                flag = True
                break
print(-1 if flag else res)