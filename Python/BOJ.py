l, r = 9 * 60, 20 * 60 + 59
for _ in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())
    l, r = max(l, h1 * 60 + m1), min(r, h2 * 60 + m2)
print('NE' if l >= r else f'TAIP\n{l // 60} {l % 60} {r // 60} {r % 60}')