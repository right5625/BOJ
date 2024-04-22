import string

res = {i : 0 for i in string.ascii_letters}
for _ in range(int(input())):
    for i in input():
        if i != ' ':
            res[i] += 1
for k, v in res.items():
    if v:
        print(k, v)