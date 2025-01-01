for i in range(int(input())):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for j in range(N - 1):
        for k in range(j + 1, N):
            if (AB[j][0] - AB[k][0]) * (AB[j][1] - AB[k][1]) < 0:
                res += 1
    print(f'Case #{i + 1}: {res}')