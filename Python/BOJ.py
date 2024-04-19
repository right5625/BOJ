for _ in range(int(input())):
    N, C, S = input().split()
    for _ in range(int(C)):
        S = S[int(N):] + S
    print(S)