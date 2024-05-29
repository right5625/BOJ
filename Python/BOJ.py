while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    nList, mList = [int(input()) for _ in range(n)], [int(input()) for _ in range(m)]
    s1, s2 = sum(nList), sum(mList)
    if (s1 - s2) % 2 == 1:
        print(-1)
    else:
        res = [[i, j] for i in nList for j in mList if i - j == (s1 - s2) // 2]
        print(-1) if not res else print(*sorted(res, key = lambda x : x[0] + x[1])[0])