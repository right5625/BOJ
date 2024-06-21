a, b, c = input().split()
print({sorted([int(a + b + c), int(a + c + b), int(b + a + c), int(b + c + a), int(c + a + b), int(c + b + a)])[i] : i + 1 for i in range(6)}[int(input())])