import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    res = ""
    if N % 2 == 1:
        res += "O"
    if N**0.5 == int(N**0.5):
        res += "S"
    print(res if res else "EMPTY")
