import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(-1 if r1 == r2 else 0)
    else:
        dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if dis < r1 + r2:
            maxr = max(r1, r2)
            minr = min(r1, r2)
            if maxr > minr + dis:
                print(0)
            elif maxr == minr + dis:
                print(1)
            else:
                print(2)
        elif dis == r1 + r2:
            print(1)
        else:
            print(0)