H, M = map(int, input().split(':'))
N = int(input())
cnt = 0
while True:
    if M % 15 == 0:
        cnt += (H if M == 0 else 1)
        if N <= cnt:
            break
    M += 1
    if M == 60:
        M = 0
        H += 1
        if H == 13:
            H = 1
print(f'{H:02d}:{M:02d}')