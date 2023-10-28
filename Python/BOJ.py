t, r, v = map(float, input().split())
print(max((t * v - 2 * r) / t, 0))