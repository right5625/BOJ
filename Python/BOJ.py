N = int(input())
X = int(input())
A = N * ((100 - X) / 100)
print(f'{(N - A) / A * 100:.6f}')