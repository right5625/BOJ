import sys
input = lambda : sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
S = []
for i in range(1, N + 1):
    S.extend([i] * int(input()))
for _ in range(Q):
    print(S[int(input())])