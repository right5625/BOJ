import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(min(n, k - 1))