from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    dic[len(input().split())] += 1
for k, v in sorted(dic.items()):
    print(k, v)
