import math

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    res = math.ceil((9000 - (a * 15 + b * 20 + c * 25)) / 40)
    print(res if res <= 100 else 'impossible')