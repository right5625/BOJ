while True:
    s = list(input().split())
    if s[0] == '#':
        break
    print(*[i if len(i) == 1 else i[0] + i[1 : -1][::-1] + i[-1] for i in s])