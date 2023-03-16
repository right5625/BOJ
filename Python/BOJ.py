import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def BFS(v1, v2):
    deq = deque([(v1, v2)])
    vst[v1][v2] = True
    cnt = 1
    while deq:
        n1, n2 = deq.popleft()
        for i in A[n1][n2]:
            if not vst[i[0]][i[1]]:
                deq.append((i[0], i[1]))
                vst[i[0]][i[1]] = True
                cnt += 1
    res.append(cnt)
    
N = int(input())
M = [list(map(int, input())) for _ in range(N)]
A = [[[] for __ in range(N)] for _ in range(N)]
vst = [[False for __ in range(N)] for _ in range(N)]
res = []
for i in range(N):
    for j in range(N):
        if M[i][j]:
            if i > 0 and M[i - 1][j]:
                A[i][j].append((i - 1, j))
            if i < N - 1 and M[i + 1][j]:
                A[i][j].append((i + 1, j))
            if j > 0 and M[i][j - 1]:
                A[i][j].append((i, j - 1))
            if j < N - 1 and M[i][j + 1]:
                A[i][j].append((i, j + 1))
for i in range(N):
    for j in range(N):
        if M[i][j] and not vst[i][j]:
            BFS(i, j)
print(len(res))
print(*sorted(res), sep = '\n')