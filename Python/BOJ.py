import sys
input = lambda : sys.stdin.readline().rstrip()

res = []
for _ in range(int(input())):
    name = input()
    if len(name) == 3:
        res.append(name)
print(sorted(res)[0])