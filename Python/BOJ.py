cur = 0
res = "See you next month"
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 1:
        cur += y
    else:
        cur -= y
        if cur < 0:
            res = "Adios"
print(res)
