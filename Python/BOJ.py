N, B = input().split()
dic = {'A': [11, 11], 'K': [4, 4], 'Q': [3, 3], 'J': [20, 2], 'T': [10, 10], '9': [14, 0], '8': [0, 0], '7': [0, 0]}
res = 0
for _ in range(int(N) * 4):
    S = input()
    res += dic[S[0]][0] if S[1] == B else dic[S[0]][1]
print(res)