for _ in range(int(input())):
    K = int(input())
    exp = 0
    while 2 ** exp < K:
        exp += 1
    if 2 ** exp == K:
        print(0)
    else:
        cnt = 0
        while K > 0:
            exp -= 1
            if K >= 2 ** exp:
                K -= 2 ** exp
            cnt += 1
        print(cnt)