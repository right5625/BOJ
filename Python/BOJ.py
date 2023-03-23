import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
flag = False
for i in range(N):
    for j in range(M):
        if T[i][j] == 0:
            if i == 0:
                if j == 0:
                    if T[i][j + 1] == -1 and T[i + 1][j] == -1:
                        flag = True
                        break
                elif j == M - 1:
                    if T[i][j - 1] == -1 and T[i + 1][j] == -1:
                        flag = True
                        break
                else:
                    if T[i][j - 1] == -1 and T[i + 1][j] == -1 and T[i][j + 1] == -1:
                        flag = True
                        break
            elif i == N - 1:
                if j == 0:
                    if T[i][j + 1] == -1 and T[i - 1][j] == -1:
                        flag = True
                        break
                elif j == M - 1:
                    if T[i][j - 1] == -1 and T[i - 1][j] == -1:
                        flag = True
                        break
                else:
                    if T[i][j - 1] == -1 and T[i - 1][j] == -1 and T[i][j + 1] == -1:
                        flag = True
                        break
            elif j == 0 and T[i - 1][j] == -1 and T[i][j + 1] == -1 and T[i + 1][j] == -1:
                flag = True
                break
            elif j == M - 1 and T[i - 1][j] == -1 and T[i][j - 1] == -1 and T[i + 1][j] == -1:
                flag = True
                break
            else:
                if T[i - 1][j] == -1 and T[i][j + 1] == -1 and T[i + 1][j] == -1 and T[i][j - 1] == -1:
                    flag = True
                    break
if flag:
    print(-1)
else:
    start = []
    for i in range(N):
        for j in range(M):
            if T[i][j] == 1:
                start.append((i, j))
    vst = [[False for __ in range(M)] for _ in range(N)]
    q = deque()
    res = []
    for i in start:
        q.append(i)
        vst[i[0]][i[1]] = True
        cnt = 0
        while q:
            v = q.popleft()
            l = []
            for j in v:
                if T[j[0]][j[1]] == 1 and j[0] 