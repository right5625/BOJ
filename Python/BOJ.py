while True:
    S = input()
    if S == '0':
        break
    prev = S[0]
    cnt = 1
    res = ''
    for cur in S[1:]:
        if prev == cur:
            cnt += 1
        else:
            res += str(cnt) + prev
            prev = cur
            cnt = 1
    res += str(cnt) + prev
    print(res)