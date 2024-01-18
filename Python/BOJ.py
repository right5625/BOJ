import sys
input = lambda : sys.stdin.readline().rstrip()

res = m = 0
for i in [int(input()) for _ in range(int(input()))][::-1]:
    if m < i:
        m = i
        res += 1
print(res)