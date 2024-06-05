while True:
    N, Z = input().split()
    if N == '#' and Z == '0':
        break
    P = int(input())
    for _ in range(int(input())):
        A, B = map(int, input().split())
        P = max(P - A, 0)
        P = min(P + B, int(Z))
    print(N, P)