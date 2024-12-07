n, m = map(int, input().split())
res = 'Yes'
for _ in range(n):
    if list(input().split()).count('A') != 1:
        res = 'No'
print(res)