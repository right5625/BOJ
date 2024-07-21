a = int(input())
b = int(input())
n, res = 1, 0
while n ** 6 <= b:
    if a <= n ** 6:
        res += 1
    n += 1
print(res)