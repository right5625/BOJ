while True:
    lst = list(map(int, input().split()))
    if lst == [-1] * 4:
        break
    if lst[0] == -1:
        if lst[2] / lst[1] == lst[3] / lst[2]:
            temp = lst[1] / (lst[3] / lst[2])
            res = int(temp) if temp == int(temp) else -1
        elif lst[2] - lst[1] == lst[3] - lst[2]:
            res = lst[1] - (lst[3] - lst[2])
        else:
            res = -1
    elif lst[1] == -1:
        if lst[2] / lst[0] == (lst[3] / lst[2]) ** 2:
            temp = lst[2] / (lst[3] / lst[2])
            res = int(temp) if temp == int(temp) else -1
        elif lst[2] - lst[0] == (lst[3] - lst[2]) * 2:
            res = lst[2] - (lst[3] - lst[2])
        else:
            res = -1
    elif lst[2] == -1:
        if (lst[1] / lst[0]) ** 2 == lst[3] / lst[1]:
            temp = lst[3] / (lst[1] / lst[0])
            res = int(temp) if temp == int(temp) else -1
        elif (lst[1] - lst[0]) * 2 == lst[3] - lst[1]:
            res = lst[3] - (lst[1] - lst[0])
        else:
            res = -1
    else:
        if lst[1] / lst[0] == lst[2] / lst[1]:
            res = int(lst[2] * (lst[1] / lst[0]))
        elif lst[1] - lst[0] == lst[2] - lst[1]:
            res = lst[2] + (lst[1] - lst[0])
        else:
            res = -1
    print(res if 1 <= res <= 10000 else -1)