while True:
    n = int(input())
    if n == 0:
        break
    print(*[int(input()) for _ in range(n)][::-1] + [0], sep = '\n')