for _ in range(int(input())):
    a, b, c = map(int, input().split())
    res = set()
    for i in range(1, a):
        if i % b == 0 or i % c == 0:
            res.add(i)
    print(f"{a} {b} {c}\n{len(res)}")
