while True:
    S = list(input().split())
    if S[0] == '#':
        break
    H = [False] * 21
    cur = int(S[0])
    H[cur] = True
    flag = False
    for i in S[1:]:
        if i[0] == 'U':
            cur += int(i[1])
        else:
            cur -= int(i[1])
        if cur < 1 or cur > 20 or H[cur]:
            flag = True
            break
        H[cur] = True
    if flag:
        print('illegal')
    elif False in H[1:]:
        for i in range(1, 21):
            if not H[i]:
                print(i, end = ' ')
        print()
    else:
        print('none')