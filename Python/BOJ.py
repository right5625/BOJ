while True:
    n = int(input())
    if n == 0:
        break
    lst = [input() for _ in range(n)]
    res = 0
    while True:
        lst = list(map(lambda x : x[1:], lst))
        if len(set(lst)) != n or '' in lst:
            break
        res += 1
    print(res)