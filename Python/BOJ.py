S = []
while True:
    try:
        S.append(len(input()))
    except:
        break
print(sum((max(S) - i) ** 2 for i in S[:-1]))
