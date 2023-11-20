import sys
input = lambda : sys.stdin.readline().rstrip()

D, C, R = map(int, input().split())
C_lst = [int(input()) for _ in range(C)]
D += sum([int(input()) for _ in range(R)])
res = R
for i in C_lst:
    if D - i < 0:
        break
    D -= i
    res += 1
print(res)