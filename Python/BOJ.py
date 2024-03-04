S = input()
print(S[1:-1] if len(S) > 2 and S[0] == S[-1] == '"' else 'CE')