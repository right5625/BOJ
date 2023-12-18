import string

dic = {i : 0 for i in string.ascii_lowercase}
input()
for i in input():
    if i not in ' ,.':
        dic[i] += 1
print(max(dic.values()))