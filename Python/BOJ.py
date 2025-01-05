S = input()
res, idx = [], 0
while idx < len(S):
    if len(set(S[idx : idx + 3])) == 3:
        res.append('C')
        idx += 3
    else:
        res.append({'R': 'S', 'B': 'K', 'L': 'H'}[S[idx]])
        idx += 1
print(''.join(res))