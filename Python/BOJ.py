for _ in range(int(input())):
    N, K = map(int, input().split())
    print((N - K) // (K - 1))
