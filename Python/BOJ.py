for i in range(int(input())):
    L, n = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    res = 1
    cur = p[L]
    while cur != 0:
        cur = p[cur]
        res += 1
    print(f'Data Set {i + 1}:\n{res}\n')