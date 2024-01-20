a, b, c = map(int, input().split())
print('YES' if c >= abs(a) + abs(b) and (c - (abs(a) + abs(b))) % 2 == 0 else 'NO')