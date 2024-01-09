W, N = input().split()
C = [list(map(int, input().split())) for _ in range(int(N))]
if W in 'LR':
    for i in range(int(N)):
        C[i] = C[i][::-1]
else:
    C = C[::-1]
for i in C:
    for j in i:
        if j in [3, 4, 6, 7, 9]:
            print('?', end = ' ')
        elif j == 2:
            print(5, end = ' ')
        elif j == 5:
            print(2, end = ' ')
        else:
            print(j, end = ' ')
    print()