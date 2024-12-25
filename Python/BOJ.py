for i in range(int(input())):
    _, L, H = map(int, input().split())
    lst = list(map(int, input().split()))
    res = 'NO'
    for j in range(L, H + 1):
        flag = True
        for k in lst:
            if j % k != 0 and k % j != 0:
                flag = False
                break
        if flag:
            res = j
            break
    print(f'Case #{i + 1}: {res}')