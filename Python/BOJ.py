A, B = map(int, input().split())
while A != B:
    A, B = abs(A - B), min(A, B)
print(A)
