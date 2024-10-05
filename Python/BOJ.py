import string

while True:
    S = input()
    if S == "#":
        break
    res = ""
    for i in S[:-1]:
        if i not in string.ascii_letters:
            res += i
        else:
            s = chr(ord(i) - (ord(S[-1]) - ord("A")))
            if (i in string.ascii_lowercase and s not in string.ascii_lowercase) or (
                i in string.ascii_uppercase and s not in string.ascii_uppercase
            ):
                s = chr(ord(s) + 26)
            res += s
    print(res)
