a, b, c = map(int, input().split())
print(c ** 2 - (max(a, b)) if c else int((a + b) ** 0.5))