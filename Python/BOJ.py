num = 1
while True:
    N = int(input())
    if N == 0:
        break
    res = 0
    for _ in range(N):
        c, b, l, n = map(int, input().split())
        res += c * 0.8 + b + l * 1.2 + n * 0.6 - (c * 15.5 + b * 32 + l * 40) / 85
    print(f"Case #{num}: RM{res:.2f}")
    num += 1
