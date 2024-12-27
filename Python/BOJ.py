n = int(input())
S = input()
res = -1
for i in range(1, n):
    if S[:i].count('L') != S[i:].count('L') and S[:i].count('O') != S[i:].count('O'):
        res = i
        break
print(res)