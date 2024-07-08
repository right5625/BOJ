for _ in range(int(input())):
    s = sum([int(S) * int(R) for _ in range(int(input())) for S, R in [input().split()]])
    print(*[i // s for i in [1296, 2592, 3888]])