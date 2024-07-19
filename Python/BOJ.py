X, Y, I = map(int, input().split())
S = [[False for _ in range(X)] for _ in range(Y)]
for _ in range(I):
    Xl, Yl, Xu, Yu = map(int, input().split())
    for i in range(Yl - 1, Yu):
        for j in range(Xl - 1, Xu):
            S[i][j] = True
print(sum([i.count(True) for i in S]))