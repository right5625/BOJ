import sys
input = lambda: sys.stdin.readline().rstrip()

res = cur = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    cur -= a
    cur += b
    res = max(res, cur)
print(res)