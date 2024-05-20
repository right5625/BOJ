N = int(input())
print(*[(N - i) * (i + 1) for i in range(N)], sep = '\n')