def DFS(n, d):
    vst[n] = True
    lst[d] = n
    for i in range(1, N + 1):
        if not vst[i]:
            DFS(i, d + 1)
    vst[n] = False
    if d == M:
        print(*lst[1 : M + 1], sep = ' ')

N, M = map(int, input().split())
vst = [False] * (N + 1)
lst = [0] * (N + 1)
for i in range(1, N + 1):
    DFS(i, 1)