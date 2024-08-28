for _ in range(int(input())):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    if 3 in a:
        a = a[::-1]
        a[a.index(3)] = 2
    b = a[a.index(2) :].copy()
    while len(b) < n + 1:
        b.extend(a[::-1][1:] + a[1:])
    print(b[: n + 1].count(0))
