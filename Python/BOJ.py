while True:
    card = []
    for _ in range(4):
        s = input().split()
        if s[0] == '#':
            exit()
        card.extend(s)
    card.reverse()
    pile = [[] for _ in range(13)]
    for i, j in enumerate(card):
        pile[i % 13].append(j)
    cur = pile[12].pop()
    cnt = 1
    while True:
        try:
            cur = pile['A23456789TJQK'.index(cur[0])].pop()
            cnt += 1
        except:
            break
    print(f'{cnt:02d},{cur}')