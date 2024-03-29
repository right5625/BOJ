X = int(input())
N = int(input())
res = 0
while X < N:
    X = X * (X % 3 + 1) if X % 3 else X + 1
    res += 1
print(res)