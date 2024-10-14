import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = []
pig = 0
for _ in range(n):
    s, i = input().split()
    if s == "pig":
        pig = max(pig, int(i))
    else:
        a.append(int(i))
print(pig + sum([i for i in a if i < pig]))
