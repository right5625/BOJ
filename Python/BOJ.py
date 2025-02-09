import sys, string
input = lambda: sys.stdin.readline().rstrip()

s = string.digits + string.ascii_lowercase
def convert(n, b):
    q, r = divmod(n, b)
    return s[r] if q == 0 else convert(q, b) + s[r]

for _ in range(int(input())):
    K, b, n = map(int, input().split())
    print(K, sum(s.index(i) ** 2 for i in convert(n, b)))