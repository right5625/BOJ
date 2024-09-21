import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
H = [int(input()) for _ in range(N)]
res = 0
for i in range(N // 2):
    if H[i] == H[i + N // 2]:
        res += 2
print(res)
