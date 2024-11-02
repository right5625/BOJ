A, B, N = map(int, input().split())
res = float("inf")
for _ in range(N):
    c, n = map(int, input().split())
    lst = list(map(int, input().split()))
    a = lst.index(A) if A in lst else -1
    b = lst.index(B) if B in lst else -1
    if a != -1 and a < b:
        res = min(res, c)
print(res if res != float("inf") else -1)
