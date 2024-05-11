n, k = map(int, input().split())
cur = save = 0
for _ in range(n):
    s = input()
    if s == 'save':
        save = cur
    elif s == 'load':
        cur = save
    elif s == 'shoot':
        cur -= 1
    else:
        cur += k
    print(cur)