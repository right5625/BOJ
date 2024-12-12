import sys
input = lambda: sys.stdin.readline().rstrip()

for c in range(int(input())):
    R, P, D = map(int, input().split())
    r = D / P
    dic = {}
    for _ in range(R):
        n, w, p = input().split()
        w, p = float(w), float(p)
        dic[n] = p
        if p == 100:
            r *= w
    print(f'Recipe # {c + 1}')
    for k, v in dic.items():
        print(f'{k} {v * r / 100:.1f}')
    print('----------------------------------------')