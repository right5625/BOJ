import sys

D = int(input())
flag = True
for i in list(map(int, sys.stdin.read().splitlines())):
    if flag and D > i:
        D += i
    else:
        flag = False
print(D)
