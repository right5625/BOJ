import string

s = string.ascii_lowercase + " "
for _ in range(int(input())):
    print("".join(s[sum(s.index(j) for j in i) % 27] for i in list(input().split())))
