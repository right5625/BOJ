import string

N = int(input())
S = input().replace('.', '-').replace('?', '-').replace('!', '-').split('-')
for i in S[:-1]:
    cnt = 0
    for j in i.strip().split():
        if j[0] in string.ascii_uppercase:
            flag = True
            for k in j[1:]:
                if k not in string.ascii_lowercase:
                    flag = False
                    break
            if flag:
                cnt += 1
    print(cnt)