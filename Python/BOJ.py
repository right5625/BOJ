import sys, math
input = lambda : sys.stdin.readline().rstrip()

res = []
for _ in range(int(input())):
    lst = list(input().split())
    if lst[0] == 'C':
        t = 1 / 3 * math.pi * float(lst[1]) ** 2 * float(lst[2])
    elif lst[0] == 'L':
        t = math.pi * float(lst[1]) ** 2 * float(lst[2])
    else:
        t = 4 / 3 * math.pi * float(lst[1]) ** 3
    res.append(t)
print(f'{max(res):.3f}')