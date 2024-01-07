N, M = map(int, input().split())
cube = [list(map(int, input().split())) for _ in range(M)]
res = 0
for i in cube:
    if cube.count([i[0] - 1, i[1], i[2]]) and cube.count([i[0] + 1, i[1], i[2]]) and cube.count([i[0], i[1] - 1, i[2]]) and cube.count([i[0], i[1] + 1, i[2]]) and cube.count([i[0], i[1], i[2] - 1]) and cube.count([i[0], i[1], i[2] + 1]):
        res += 1
print(res)