for _ in range(int(input())):
    S = input()
    print([S[i : i + 3] == "WOW" for i in range(len(S) - 2)].count(True))
