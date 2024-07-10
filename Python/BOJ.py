import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
k, m1, m2 = map(int, input().split())
res = 0
for _ in range(n):
    s = list(map(int, input().split()))
    for i in s[2:]:
        if max(s[0], i * m2) > min(s[0] * k, i * m1):
            res += 1
print(res)