n = int(input())
for i in range(n):
    print(*[i * n + j for j in range(1, n + 1)]) if i % 2 == 0 else print(*[i * n + j for j in range(1, n + 1)][::-1])