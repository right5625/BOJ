N, K = map(int, input().split())
h = m = s = res = 0
while h < N + 1:
    if K in [h // 10, h % 10, m // 10, m % 10, s // 10, s % 10]:
        res += 1
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
print(res)