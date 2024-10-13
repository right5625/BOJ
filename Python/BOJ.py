X, A, B = int(input()), int(input()), int(input())
res = X * A
if B:
    res += int(input()) if A else sum([int(input()) for _ in range(X)])
print(res)
