for _ in range(int(input())):
    S = input()
    print(sorted([S[i:] + S[:i] for i in range(len(S))])[0])
