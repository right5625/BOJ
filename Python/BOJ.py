for i in range(int(input())):
    S = list(input().split())
    cur, res = int(S[1][0]), 0
    for j in range(1, int(S[0]) + 1):
        if j > cur:
            res += j - cur
            cur += j - cur
        cur += int(S[1][j])
    print(f'Case #{i + 1}: {res}')