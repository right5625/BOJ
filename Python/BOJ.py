while True:
    n, m, c = map(int, input().split())
    if n == m == c == 0:
        break
    print(((n - 7) // 2) * ((m - 7) // 2) + ((n - 6) // 2) * ((m - 6) // 2) if c == 1 else ((n - 7) // 2) * ((m - 6) // 2) + ((n - 6) // 2) * ((m - 7) // 2))