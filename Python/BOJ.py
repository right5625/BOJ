import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    N = int(input())
    AB = list(map(int, input().split()))
    P = int(input())
    res = [0] * P
    for j in range(P):
        C = int(input())
        for k in range(0, N * 2, 2):
            if AB[k] <= C <= AB[k + 1]:
                res[j] += 1
    print(f'Case #{i + 1}:', *res)
    input()