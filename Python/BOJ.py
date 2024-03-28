N = int(input())
A = [input() for _ in range(N)]
B = ['' for _ in range(max([len(i) for i in A]))]
for i in A:
    for j in range(len(B)):
        try:
            B[j] += i[j]
        except:
            pass
res = ''
for i in B:
    t = 0
    for j in i:
        t += ord(j)
    res += chr(t // len(i))
print(res)