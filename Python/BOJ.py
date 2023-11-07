import sys
input = lambda : sys.stdin.readline().rstrip()

for i in range(int(input())):
    n = int(input())
    s = set(input())
    res = 0
    for _ in range(n):
        for j in set(input()):
            if j in s:
                res += 1
                break
    print(f'Data Set {i + 1}:\n{res}\n')