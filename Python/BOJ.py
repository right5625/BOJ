x, y = map(int, input().split())
x, y = bin(x)[2:].zfill(16), bin(y)[2:].zfill(16)
print(int("".join([x[i] if j == 0 else y[i] for i in range(16) for j in range(2)]), 2))
