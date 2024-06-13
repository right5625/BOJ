N, M = map(int, input().split())
S = [input() for _ in range(N)]
for i in S:
    lst = ' '.join(i.split('.')).split()
    if not lst:
        print(0)
    else:
        for j in lst:
            print(len(j), end = ' ')
        print()
for i in list(zip(*S)):
    lst = ' '.join(''.join(i).split('.')).split()
    if not lst:
        print(0)
    else:
        for j in lst:
            print(len(j), end = ' ')
        print()