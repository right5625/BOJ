S = input()
print(len(S.replace(''.join(sorted(list(set(S)))), '', 1)))