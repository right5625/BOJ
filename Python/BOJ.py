import string

J, N = map(int, input().split())
res = 0
for _ in range(N):
    j = 0
    for i in input():
        if i in string.ascii_uppercase:
            j += 4
        elif i == ' ':
            j += 1
        else:
            j += 2
    if j <= J:
        res += 1
print(res)