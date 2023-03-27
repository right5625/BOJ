import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def BFS(s1, s2):
    q = deque()
    q.append((s1, s2, 0))
    vst[s1][s2] = True
    mx = [-2, -1, 1, 2, 2, 1, -1, -2]
    my = [-1, -2, -2, -1, 1, 2, 2, 1]
    while q:
        ny, nx, cnt = q.popleft()
        if ny == e1 and nx == e2:
            return cnt
        for j in range(8):
            x = nx + mx[j]
            y = ny + my[j]
            if 0 <= x < l and 0 <= y < l and not vst[y][x]:
                q.append((y, x, cnt + 1))
                vst[y][x] = True
                
for _ in range(int(input())):
    l = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    vst = [[False for __ in range(l)] for _ in range(l)]
    print(BFS(s1, s2))