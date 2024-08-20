for _ in range(int(input())):
    N, K = map(int, input().split())
    cur = K
    while cur < N:
        cur += K - 1
    print(cur - N)