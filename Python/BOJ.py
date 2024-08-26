while True:
    n = int(input())
    if n == 0:
        break
    res = 0
    for i in range(1, n + 1):
        if i**3 > n:
            break
        res = max(res, i**3)
    for i in range(1, n + 1):
        if i * (i + 1) * (i + 2) // 6 > n:
            break
        res = max(res, i * (i + 1) * (i + 2) // 6)
    for i in range(1, n + 1):
        if i**3 > n:
            break
        for j in range(1, n + 1):
            if i**3 + j * (j + 1) * (j + 2) // 6 > n:
                break
            res = max(res, i**3 + j * (j + 1) * (j + 2) // 6)
    print(res)
