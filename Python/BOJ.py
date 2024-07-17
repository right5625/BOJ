while True:
    n = int(input())
    if not n:
        break
    a = list(map(int, input().split()))
    res = temp = sum(a[:3])
    for i in range(n - 3):
        temp = temp - a[i] + a[i + 3]
        res = max(res, temp)
    print(res)