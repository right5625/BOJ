N, S = input().split()
res = 0
for _ in range(int(N)):
    s, n = input().split()
    if S in list(s.split('_')):
        res += int(n)
print(res)