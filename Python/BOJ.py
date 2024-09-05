S = input()
res = []
for _ in range(int(input())):
    s = input()
    flag = True
    for i, j in zip(S, s):
        if i != "*" and i != j:
            flag = False
            break
    if flag:
        res.append(s)
print(len(res))
print(*res, sep="\n")
