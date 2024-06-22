while True:
    s1, s2 = input().split()
    if s1 == s2 == '#':
        break
    res = [0, 0]
    for _ in range(int(input())):
        c1, c2 = input().split()
        if c1 == c2:
            res[0] += 1
        else:
            res[1] += 1
    print(f'{s1} {res[0]} {s2} {res[1]}')