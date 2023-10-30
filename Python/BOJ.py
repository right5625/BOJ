lst = []
for _ in range(6):
    N, M = map(int, input().split())
    lst.append(N + M * 10)
print(max(max(lst[1:]) - lst[0] + 1, 0))