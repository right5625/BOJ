N = int(input())
X, S = map(int, input().split())
res = 'NO'
for _ in range(N):
    c, p = map(int, input().split())
    if X >= c and S < p:
        res = 'YES'
print(res)