N = int(input())
n, d = 10, -1
while N > n:
    N = round(N + 0.00000001, d)
    n *= 10
    d -= 1
print(int(N))