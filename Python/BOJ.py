x, y = map(int, input().split())
d = int(input())
cm = x * 100 + y
b = (cm - d * 2) // 4
a = b + d
print(f'{a // 100} {a % 100}\n{b // 100} {b % 100}')