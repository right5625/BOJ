import math

d, h = map(float, input().split())
print(math.pi * 2 * (d / 2 + 5) * h + math.pi * (d / 2 + 5) ** 2)