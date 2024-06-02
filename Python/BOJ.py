def fac(n):
    return 1 if n == 1 else n * fac(n - 1)

for _ in range(int(input())):
    print(str(fac(int(input())))[-1])