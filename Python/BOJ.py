import string

while True:
    S = input()
    if S == "0":
        break
    N, S = S.split()
    res = ""
    for i in S[::-1]:
        s = ord(i) - ord("A") + int(N)
        if i == "_":
            s -= 4
        elif i == ".":
            s += 46
        res += (string.ascii_uppercase + "_.")[s % 28]
    print(res)
