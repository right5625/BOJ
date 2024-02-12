res = 0
for _ in range(int(input())):
    S = input()
    res = max(res, S.count('for') + S.count('while'))
print(res)