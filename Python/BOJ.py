S = input()
if 'A' in S:
    print(S.replace('B', 'A').replace('C', 'A').replace('D', 'A').replace('F', 'A'))
elif 'B' in S:
    print(S.replace('C', 'B').replace('D', 'B').replace('F', 'B'))
elif 'C' in S:
    print(S.replace('D', 'C').replace('F', 'C'))
else:
    print('A' * len(S))