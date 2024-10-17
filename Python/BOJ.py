from math import log10

for _ in range(int(input())):
    t, n = input().split(" = ")
    print(f'{-log10(float(n)) if t == "H" else 14 + log10(float(n)):.2f}')
