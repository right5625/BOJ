N = int(input())
S = input()
while 'PS4' in S or 'PS5' in S:
    S = S.replace('PS4', 'PS').replace('PS5', 'PS')
print(S)