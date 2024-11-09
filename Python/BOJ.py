import string

for _ in range(int(input())):
    s = input()
    for _ in range(int(input())):
        w = input()
        res = "YES"
        for i in string.ascii_uppercase:
            if s.count(i) < w.count(i):
                res = "NO"
                break
        print(res)
