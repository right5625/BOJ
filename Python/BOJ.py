x1, x2, n = map(int, input().split())
print('YES' if x1 == x2 else 'NO') if n == 0 else print('YES' if x1 > x2 and (x1 - x2) % 2 == 0 and (x1 - x2) // 2 >= n else 'NO')