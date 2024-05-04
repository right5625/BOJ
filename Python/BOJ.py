while True:
    n = int(input())
    if n == 0:
        break
    a = list(input() for _ in range(n))
    key = sorted(list(i.lower() for i in a))[0]
    for i in a:
        if key == i.lower():
            print(i)
            break