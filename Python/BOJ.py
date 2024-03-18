N = input()
S = input()
T = input()
res = 0
for i, j in zip(S, T):
    if i != j:
        res += 1
print(res)