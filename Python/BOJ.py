import sys

input = lambda: sys.stdin.readline().rstrip()

rect = []
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rect.append([x2 - x1, y2 - y1])
res = 0
for i in range(n):
    for j in range(i + 1, n):
        if not (
            (rect[i][0] <= rect[j][0] and rect[i][1] <= rect[j][1])
            or (rect[i][0] <= rect[j][1] and rect[i][1] <= rect[j][0])
            or (rect[j][0] <= rect[i][0] and rect[j][1] <= rect[i][1])
            or (rect[j][0] <= rect[i][1] and rect[j][1] <= rect[i][0])
        ):
            res += 1
print(res)
