import sys, math
input = lambda : sys.stdin.readline().rstrip()

dots = {'R' : 0.55, 'G' : 0.7, 'B' : 0.8, 'Y' : 0.85, 'O' : 0.9, 'W' : 0.95}
for _ in range(int(input())):
    price, dot, coupon, pay = input().split()
    price = float(price) * dots[dot]
    if coupon == 'C':
        price *= 0.95
    if pay == 'C':
        if price - math.floor(price * 10) / 10 < 0.06:
            price = math.floor(price * 10) / 10
        else:
            price = math.ceil(price * 10) / 10
    else:
        price = round(price, 2)
    print(f'${price:.2f}')