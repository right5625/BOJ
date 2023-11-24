from math import ceil

h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())
r1 = ceil(max((h2 - d1), 0) / d1) * t1
r2 = ceil(max((h1 - d2), 0) / d2) * t2
print('draw') if r1 == r2 else print('player one' if r1 < r2 else 'player two')