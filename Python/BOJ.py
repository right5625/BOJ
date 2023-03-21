import sys
input = lambda : sys.stdin.readline().rstrip()

cs = 1
while True:
    S = input()
    if S == '0':
        break
    r, w, l = map(int, S.split())
    print(f'Pizza {cs} does not fit on the table.' if r * 2 < (w ** 2 + l ** 2) ** 0.5 else f'Pizza {cs} fits on the table.')
    cs += 1