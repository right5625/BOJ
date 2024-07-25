for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] <= b[j]:
                res = max(res, abs(i - j))
    print(f'The maximum distance is {res}\n')