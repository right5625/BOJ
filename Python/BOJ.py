x, s = map(int, input().split())
cur = cnt = 0
while s > 1 and cur < x:
    cur += s
    cnt += 1
    s //= 2
print(cnt + max(x - cur, 0))