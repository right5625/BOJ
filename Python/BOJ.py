while True:
    s = input()
    if s == '#':
        break
    res = 'not possible'
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        if t == t[::-1]:
            res = t
            break
    print(res)