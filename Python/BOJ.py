import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    lst = [False] * (n + 1)
    lst[m] = True
    for _ in range(n - 2):
        lst[int(input())] = True
    for i in range(1, n + 1):
        if not lst[i]:
            print(i)
            break