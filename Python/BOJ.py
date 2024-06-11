import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

res = defaultdict(int)
for _ in range(int(input())):
    g, r = map(int, input().split())
    res[r] = max(res[r], g)
print(len(res))