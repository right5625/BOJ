lst = [list(map(float, input().split())) for _ in range(int(input()))]
for _ in range(int(input())):
    p = int(input())
    path = list(map(int, input().split()))
    res = 0
    for i in range(p - 1):
        res += (
            (lst[path[i]][0] - lst[path[i + 1]][0]) ** 2
            + (lst[path[i]][1] - lst[path[i + 1]][1]) ** 2
        ) ** 0.5
    print(round(res))
