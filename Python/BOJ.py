res = [1001, 1001]
for _ in range(int(input())):
    x, y = map(int, input().split())
    if res[1] > y:
        res = [x, y]
print(*res)