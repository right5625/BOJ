import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    l = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    vst = [[False for __ in range(l)] for _ in range(l)]
    q = deque([[(s1, s2)]])
    vst[s1][s2] = True
    res = 0
    while q:
        v = q.popleft()
        lst = []
        for i in v:
            if i[0] == e1 and i[1] == e2:
                res -= 1
                lst.clear()
                break
            if i[0] > 1 and i[1] > 0 and not vst[i[0] - 2][i[1] - 1]:
                lst.append((i[0] - 2, i[1] - 1))
                vst[i[0] - 2][i[1] - 1] = True
            if i[0] > 0 and i[1] > 1 and not vst[i[0] - 1][i[1] - 2]:
                lst.append((i[0] - 1, i[1] - 2))
                vst[i[0] - 1][i[1] - 2] = True
            if i[0] < l - 1 and i[1] > 1 and not vst[i[0] + 1][i[1] - 2]:
                lst.append((i[0] + 1, i[1] - 2))
                vst[i[0] + 1][i[1] - 2] = True
            if i[0] < l - 2 and i[1] > 0 and not vst[i[0] + 2][i[1] - 1]:
                lst.append((i[0] + 2, i[1] - 1))
                vst[i[0] + 2][i[1] - 1] = True
            if i[0] < l - 2 and i[1] < l - 1 and not vst[i[0] + 2][i[1] + 1]:
                lst.append((i[0] + 2, i[1] + 1))
                vst[i[0] + 2][i[1] + 1] = True
            if i[0] < l - 1 and i[1] < l - 2 and not vst[i[0] + 1][i[1] + 2]:
                lst.append((i[0] + 1, i[1] + 2))
                vst[i[0] + 1][i[1] + 2] = True
            if i[0] > 0 and i[1] < l - 2 and not vst[i[0] - 1][i[1] + 2]:
                lst.append((i[0] - 1, i[1] + 2))
                vst[i[0] - 1][i[1] + 2] = True
            if i[0] > 1 and i[1] < l - 1 and not vst[i[0] - 2][i[1] + 1]:
                lst.append((i[0] - 2, i[1] + 1))
                vst[i[0] - 2][i[1] + 1] = True
        if lst:
            q.append(lst)
        res += 1
    print(res)