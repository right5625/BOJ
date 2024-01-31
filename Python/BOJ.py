N, M = map(int, input().split())
L = [0] + list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        L[b] = c
    elif a == 2:
        for i in range(b, c + 1):
            L[i] = abs(L[i] - 1)
    elif a == 3:
        for i in range(b, c + 1):
            L[i] = 0
    else:
        for i in range(b, c + 1):
            L[i] = 1
print(*L[1:])