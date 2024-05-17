k = int(input())
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
res = 'NO'
for i in a:
    if s - i >= k:
        res = 'YES'
        break
print(res)