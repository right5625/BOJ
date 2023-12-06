A, B = map(int, input().split())
try:
    print(int(24 / (24 / A + 24 / B)))
except:
    print(0)