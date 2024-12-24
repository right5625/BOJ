_, X = map(int, input().split())
res = 'YES'
for _ in range(int(input())):
    input()
    if X not in list(map(int, input().split())):
        res = 'NO'
print(res)