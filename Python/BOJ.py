for c in range(int(input())):
    N = int(input())
    AB = list(map(int, input().split()))
    res = []
    for i in [int(input()) for _ in range(int(input()))]:
        cnt = 0
        for j in range(0, N * 2, 2):
            if AB[j] <= i <= AB[j + 1]:
                cnt += 1
        res.append(cnt)
    print(f'Case #{c + 1}:', *res)
    input()
