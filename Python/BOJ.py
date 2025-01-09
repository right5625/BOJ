N, R = map(int, input().split())
res = set(i for i in range(1, N + 1)) - set(map(int, input().split()))
print(*sorted(list(res)) if res else '*')