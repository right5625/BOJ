for _ in range(int(input())):
    input()
    res = 0
    for i, j in zip(list(map(int, input().split())), list(map(int, input().split()))):
        if i != j:
            res += 1
    print(res)