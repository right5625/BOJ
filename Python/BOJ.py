N, M = map(int, input().split())
lst = list(zip(*[list(input()) for _ in range(N)]))
res = 'ESCAPE FAILED'
for i in range(M):
    if len(set(lst[i])) == 1 and lst[i][0] == 'X':
        res = i + 1
        break
print(res)