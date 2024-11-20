for _ in range(int(input())):
    S = list(input().strip().split())
    try:
        if len(S) > 1 or "-" in S[0] or "." in S[0]:
            res = "invalid input"
        else:
            res = int(S[0])
    except:
        res = "invalid input"
    print(res)
