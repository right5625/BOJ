import sys

input = lambda: sys.stdin.readline().rstrip()

res = 0
for _ in range(int(input())):
    A, B = map(int, input().split())
    res += A - B
    print(res)
