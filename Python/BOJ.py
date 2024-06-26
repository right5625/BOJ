for i in range(int(input())):
    C = int(input())
    I = int(input())
    P = list(map(int, input().split()))
    flag = True
    for j in range(I):
        for k in range(I):
            if flag and j != k and P[j] + P[k] == C:
                print(f'Case #{i + 1}: {j + 1} {k + 1}')
                flag = False