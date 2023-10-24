x1, x2, n = map(int, input().split())
if (n == 0 and x1 == x2) or ((x1 - (n - 1)) - (x2 + (n - 1))) > 0 and ((x1 - (n - 1)) - (x2 + (n - 1))) % 2 == 0