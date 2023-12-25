N = int(input())
X, Y, R = map(int, input().split())
res = [0, 0]
for _ in range(N):
    T = int(input())
    if X - R < T < X + R:
        res[0] += 1
    elif X - R == T or X + R == T:
        res[1] += 1
print(*res)