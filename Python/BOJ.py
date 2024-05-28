K = int(input())
for i in ['G...', '.I.T', '..S.']:
    for _ in range(K):
        for j in i:
            print(j * K, end = '')
        print()