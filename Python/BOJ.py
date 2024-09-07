for _ in range(int(input())):
    cnt = 0
    res = [0, 0, 0, 0]
    for i in input():
        if i == "U":
            res[1] += 1
            res[3] += 1
        elif i == "R":
            res[0] += 1
            res[2] += 1
        elif i == "D":
            res[1] -= 1
            res[3] -= 1
        elif i == "L":
            res[0] -= 1
            res[2] -= 1
        else:
            cnt += 1
    print(res[0] - cnt, res[1] - cnt, res[2] + cnt, res[3] + cnt)
