from collections import defaultdict

dic = defaultdict(int)
for i in input():
    dic[i] += 1
print(sum(sorted(dic.values())[:-2]))