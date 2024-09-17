a = sum([(i + 1) * j for i, j in enumerate(list(map(int, input().split())))])
b = sum([(i + 1) * j for i, j in enumerate(list(map(int, input().split())))])
print(0) if a == b else print(1 if a > b else 2)
