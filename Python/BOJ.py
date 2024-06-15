while True:
    n = int(input())
    if not n:
        break
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = [0, 0]
    for a, b in zip(A, B):
        if b - a == 1:
            if b == 2:
                res[0] += 6
            else:
                res[0] += a + b
        elif a - b == 1:
            if a == 2:
                res[1] += 6
            else:
                res[1] += a + b
        elif a != b:
            if a > b:
                res[0] += a
            else:
                res[1] += b
    print(f'A has {res[0]} points. B has {res[1]} points.\n')