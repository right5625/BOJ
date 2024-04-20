while True:
    n = int(input())
    if n == -1:
        break
    print(int('0b' + bin(n)[2:].zfill(32)[::-1], 2))