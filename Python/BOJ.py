for _ in range(int(input())):
    S = list(input().split())
    res = 0
    for i in range(len(S)):
        if S[i] in ['u', 'ur'] or (i < len(S) - 1 and ' '.join(S[i:i + 2]) in ['would of', 'should of']) or 'lol' in S[i]:
            res += 10
    print(res)