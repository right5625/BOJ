N = int(input())
K = [list(map(int, input().split())) for _ in range(N)]
col = [K[i][0] for i in range(N)]
(
    print(0 if col == sorted(col) else 3)
    if K[0] == sorted(K[0])
    else print(1 if col == sorted(col) else 2)
)
