while True:
    n = int(input())
    if not n:
        break
    a = sorted(list(map(int, input().split())))
    res = float('inf')
    for i in range(n - 1):
        res = min(res, a[i + 1] - a[i])
    print(res)