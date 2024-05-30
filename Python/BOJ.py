while True:
    C = int(input())
    if not C:
        break
    res = [[1, C]]
    for i in range(2, int(C ** 0.5) + 1):
        if C % i == 0:
            res.append([i, C // i])
    res = sorted(res, key = lambda x : x[0] + x[1])[0]
    print(f'Minimum perimeter is {(res[0] + res[1]) * 2} with dimensions {res[0]} x {res[1]}')