N = int(input())
res = [0] * N
for i in list(zip(*[list(map(int, input().split())) for _ in range(N)])):
    for j in range(N):
        if i.count(i[j]) == 1:
            res[j] += i[j]
print(*res, sep = '\n')