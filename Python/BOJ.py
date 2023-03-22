import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
vst = [False] * 100001
q = deque([[N]])
vst[N] = True
res = 0
while q:
    v = q.popleft()
    l = []
    res += 1
    for i in v:
        if i == K:
            l.clear()
            break
        if i > 0 and not vst[i - 1]:
            l.append(i - 1)
            vst[i - 1] = True
        if i < 100000 and not vst[i + 1]:
            l.append(i + 1)
            vst[i + 1] = True
        if i * 2 < 100001 and not vst[i * 2]:
            l.append(i * 2)
            vst[i * 2] = True
    if l:
        q.append(l)
print(res - 1)