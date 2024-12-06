S = list(input().split('('))
print(f'{S[0]}\n-' if len(S) == 1 else f'{S[0].rstrip()}\n{S[1][:-1]}')