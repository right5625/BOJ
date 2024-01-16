S = list(input().split('|'))
C = A = 0
for i in S:
    if i[0] in 'CFG':
        C += 1
    elif i[0] in 'ADE':
        A += 1
if C == A:
    if S[-1][-1] in 'CFG':
        C += 1
    elif S[-1][-1] in 'ADE':
        A += 1
print('C-major' if C > A else 'A-minor')