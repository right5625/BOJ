white = []
black = []
n = 0
for i in range(8):
    for j in range(1, 9):
        if j % 2 == n:
            white.append('ABCDEFGH'[i] + str(j))
            white.append(str(i * 8 + j))
        else:
            black.append('ABCDEFGH'[i] + str(j))
            black.append(str(i * 8 + j))
    n = abs(n - 1)
for _ in range(int(input())):
    n1, n2 = input().split()
    print('YES' if (n1 in white and n2 in white) or (n1 in black and n2 in black) else 'NO')