n = int(input())
f = list(map(int, input().split()))
res = 'NIE'
for i in range(n - 2):
    if len(set(f[i : i + 3])) == 3:
        res = 'TAK'
        break
print(res)