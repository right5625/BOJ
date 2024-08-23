for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(0, i):
            if a[j] <= a[i]:
                res += 1
    print(res)
