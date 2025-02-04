N = int(input())
X = int(input())
res = 0
for _ in range(N):
    P = list(map(int, input().split()))
    if abs(P[0] - P[1]) <= X:
        res += max(P[0], P[1])
    else:
        P3 = int(input())
        res += P3
print(res)