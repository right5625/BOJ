pa = pb = 0
res = "yes"
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < pa or b < pb:
        res = "no"
    pa, pb = a, b
print(res)
