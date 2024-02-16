S = [input() for _ in range(int(input()))]
print(''.join([S[0][i] if len(set([j[i] for j in S])) == 1 else '?' for i in range(len(S[0]))]))