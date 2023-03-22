import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
vst = [[False for __ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if T[i][j] == 0:
            flag = False
            if i == 0:
                if j == 0:
                    if T[0][1] == -1 and T[1][0] == -1:
                        flag = True
                        break
                elif j == M - 1:
                    if T[0][M - 2] == -1 and T[1][M - 1] == -1:
                        flag = True
                        break
                else:
                    if T[0][j - 1] == -1 and T[1][j] == -1 and T[0][j + 1] == -1:
                        flag = True
                        break
                

start = []
for i in range(N):
    for j in range(M):
        if T[i][j] == 1:
            start.append((i, j))
q = deque(start)
