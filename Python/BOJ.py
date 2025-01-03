import string

for _ in range(int(input())):
    S = input()
    flag = True
    for i in S[:4] + S[5:]:
        if not i in string.digits.replace('0', ''):
            flag = False
            break
    if flag and len(set(S[:2])) == 1 and S[4] in string.ascii_uppercase:
        print(S)