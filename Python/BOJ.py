N = int(input())
lst = list(map(int, input().split()))
apr = opp = inv = 0
for i in lst:
    if i == 1:
        apr += 1
    elif i == -1:
        opp += 1
    else:
        inv += 1
if (N % 2 == 0 and N // 2 <= inv) or (N % 2 == 1 and N // 2 < inv):
    print('INVALID')
elif apr > opp:
    print('APPROVED')
else:
    print('REJECTED')