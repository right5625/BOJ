AB = {'A' : 0, 'B' : 0}
while True:
    S = input().split()
    if S[0] == '1':
        AB[S[1]] = int(S[2]) if S[2] not in 'AB' else AB[S[2]]
    elif S[0] == '2':
        print(AB[S[1]])
    elif S[0] == '3':
        AB[S[1]] += int(S[2]) if S[2] not in 'AB' else AB[S[2]]
    elif S[0] == '4':
        AB[S[1]] *= int(S[2]) if S[2] not in 'AB' else AB[S[2]]
    elif S[0] == '5':
        AB[S[1]] -= int(S[2]) if S[2] not in 'AB' else AB[S[2]]
    elif S[0] == '6':
        AB[S[1]] //= int(S[2]) if S[2] not in 'AB' else AB[S[2]]
    else:
        break