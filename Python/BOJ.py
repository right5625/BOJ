while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 == Y1 == X2 == Y2 == 0:
        break
    print(0) if X1 == X2 and Y1 == Y2 else print(1 if X1 == X2 or Y1 == Y2 or abs(X2 - X1) == abs(Y2 - Y1) else 2)