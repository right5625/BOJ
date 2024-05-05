N = input()
res = 'NO'
for i in range(1, len(N)):
    a = b = 1
    for j in list(map(int, N[:i])):
        a *= j
    for j in list(map(int, N[i:])):
        b *= j
    if a == b:
        res = 'YES'
        break
print(res)