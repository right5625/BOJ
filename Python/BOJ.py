for i in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    res = 0
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    if a ^ b ^ c ^ d == K:
                        res += 1
    print(f'Case #{i + 1}: {res}')