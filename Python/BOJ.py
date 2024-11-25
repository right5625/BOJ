for _ in range(int(input())):
    S = input()
    res = 'YES'
    for i in set(input()):
        if i not in S:
            res = 'NO'
            break
    print(res)