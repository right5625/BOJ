a = set(list(map(int, input().split()))[1:])
res = 0
for _ in range(int(input())):
    if not a.intersection(set(list(map(int, input().split()))[1:])):
        res += 1
print(res)