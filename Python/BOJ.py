N = int(input())
j1, j2, i1, i2 = input(), input(), input(), input()
res = ""
for i in range(N):
    if j1[i] == i1[i]:
        if j2[i] != i2[i]:
            res = "htg!"
            break
        res += j2[i]
print(res)
