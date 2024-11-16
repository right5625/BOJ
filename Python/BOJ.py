P = [int(input()) for _ in range(int(input()))]
print(min(P) - min(min(P), max(P) // 2))
