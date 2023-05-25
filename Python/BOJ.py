import sys
input = lambda : sys.stdin.readline().rstrip()

for c in range(int(input())):
    S, M, F = input().split()
    M = int(M[0]) * 12 + int(M[2 : -1])
    F = int(F[0]) * 12 + int(F[2 : -1])
    R = M + F + 5 if S == 'B' else M + F - 5
    if R / 2 == R // 2:
        start = R // 2 - 4
        end = start + 8
    else:
        start = R // 2 - 3
        end = start + 7
    print(f'Case #{c + 1}: {start // 12}\'{start % 12}" to {end // 12}\'{end % 12}"')