c, r = map(int, input().split())
cur = [0, 0]
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    cur[0] = min(max(cur[0] + a, 0), c)
    cur[1] = min(max(cur[1] + b, 0), r)
    print(*cur)