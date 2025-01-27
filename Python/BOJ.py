import math

while True:
    V, N, M = input().split()
    if V == N == M == '0':
        break
    V, N, M = float(V), N.zfill(4), M.zfill(4)
    res = V
    if N[-4:] == M[-4:]:
        res *= 3000
    elif N[-3:] == M[-3:]:
        res *= 500
    elif N[-2:] == M[-2:]:
        res *= 50
    elif (math.ceil(int(N[-2:]) / 4) == math.ceil(int(M[-2:]) / 4)) or (N[-2:] in ['97', '98', '99', '00'] and M[-2] in ['97', '98', '99', '00']):
        res *= 16
    else:
        res *= 0
    print(f'{res:.2f}')