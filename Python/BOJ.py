from collections import defaultdict

res = defaultdict(int)
for _ in range(int(input())):
    for i in input():
        if i != ' ':
            res[i] += 1
for k, v in res.items():
    print(k, v)