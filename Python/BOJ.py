for _ in range(int(input())):
    x, k, h = map(int, input().split())
    print(format(int(x * min(k - h, 140) + x * max(k - h - 140, 0) * 1.5 + x * h * 2), ','))