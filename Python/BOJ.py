def star(n, p, c):
    if n == 3:
        res[p].append(c * 3)
        res[p + 1].append(c + ' ' + c)
        res[p + 2].append(c * 3)
        return
    for i in range(3):
        star(n // 3, n // 3 * i + p, c)
        star(n // 3, n // 3 * i + p, ' ') if i % 2 == 1 else star(n // 3, n // 3 * i + p, c)    
        star(n // 3, n // 3 * i + p, c)

N = int(input())
res = [[] for _ in range(N)]
star(N, 0, '*')
for i in res:
    print(''.join(i))