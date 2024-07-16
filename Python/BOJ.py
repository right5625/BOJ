import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    L, R, S = map(int, input().split())
    print(min((S - L) * 2 + 1, (R - S) * 2))