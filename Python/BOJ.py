import sys
input = lambda : sys.stdin.readline().rstrip()

for c in range(int(input())):
    B = int(input())
    S = input().replace('O', '0').replace('I', '1')
    print(f'Case #{c + 1}: ', end = '')
    print(*[chr(int(S[i * 8 : (i + 1) * 8], 2)) for i in range(B)], sep = '')