import sys
input = lambda : sys.stdin.readline().rstrip()

res = {i : 0 for i in range(1, 13)}
for _ in range(int(input())):
    res[int(input().split()[1].split('/')[1])] += 1
for k, v in res.items():
    print(k, v)