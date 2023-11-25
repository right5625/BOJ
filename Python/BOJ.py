import sys
input = lambda : sys.stdin.readline().rstrip()

res = prevl = prevr = 0
for _ in range(int(input())):
    l, r = map(int, input().split())
    if l and r and l == r:
        res += 1
    if l and l == prevl:
        res += 1
    if r and r == prevr:
        res += 1
    prevl, prevr = l, r
print(res)