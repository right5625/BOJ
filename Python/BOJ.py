S = input()
grade = {'A+' : 4.5, 'A' : 4, 'B+' : 3.5, 'B' : 3, 'C+' : 2.5, 'C' : 2, 'D+' : 1.5, 'D' : 1, 'F' : 0}
res = cnt = idx = 0
while idx < len(S) - 1:
    if S[idx + 1] == '+':
        res += grade[S[idx] + '+']
        idx += 2
    else:
        res += grade[S[idx]]
        idx += 1
    cnt += 1
if idx == len(S) - 1:
    res += grade[S[idx]]
    cnt += 1
print(res / cnt)