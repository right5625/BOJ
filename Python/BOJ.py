for _ in range(int(input())):
    x = int(input())
    inc = 1
    while x > 10 ** inc:
        x = int(round(x + 0.1, -inc))
        inc += 1
    print(x)