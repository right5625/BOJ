import sys
input = lambda : sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
L = list(map(int, input().split()))
for _ in range(Q):
    A, B, C = map(int, input().split())
    if A == 1:
        L[B - 1] = C
    else:
        print(abs(L[C - 1] - L[B - 1]))