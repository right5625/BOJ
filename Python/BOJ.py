import string

for _ in range(int(input())):
    n = int(input())
    s = list(string.ascii_lowercase)
    res = ""
    for i in list(map(int, input().split())):
        res += s.pop(i)
        s = [res[-1]] + s
    print(res)
