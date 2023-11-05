n = int(input())
a = input()
b = input()
res = 0
for i, j in zip(a, b):
    d = abs(ord(i) - ord(j))
    res += 26 - d if d > 12 else d
print(res)