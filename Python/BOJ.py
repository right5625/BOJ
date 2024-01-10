p = sorted([float(input()) for _ in range(10)])[::-1]
res = 1
for i in range(9):
    res *= (p[i] / (i + 1))
print(res * 10 ** 9)