while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = list(map(int, input().split()))
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] <= m:
                res = max(res, a[i] + a[j])
    print(res if res != 0 else 'NONE')