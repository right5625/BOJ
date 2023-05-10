n = int(input())
lst = list(map(int, input().split()))
res = [1] + [lst.index(i) + 2 for i in range(n - 1)]
print(*res)