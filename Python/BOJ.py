for i in range(int(input())):
    m = int(input())
    a = []
    while len(a) != m * 2:
        a.extend(list(map(int, input().split())))
    res = [0, 0]
    for j in range(0, m * 2, 2):
        if a[j] > a[j + 1]:
            if a[j] - a[j + 1] == 1:
                res[1] += a[j] + a[j + 1] if a[j] != 2 else 6
            else:
                res[0] += a[j]
        elif a[j + 1] > a[j]:
            if a[j + 1] - a[j] == 1:
                res[0] += a[j + 1] + a[j] if a[j + 1] != 2 else 6
            else:
                res[1] += a[j + 1]
    print(f"Game {i + 1}: Tessa {res[0]} Danny {res[1]}")
