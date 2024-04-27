S = input()
res = 0
for i in range(0, len(S), 3):
    if S[i] != 'P':
        res += 1
    if S[i + 1] != 'E':
        res += 1
    if S[i + 2] != 'R':
        res += 1
print(res)