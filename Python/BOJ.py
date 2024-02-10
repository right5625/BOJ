N = input()
n = N[-1] + N[:-1]
res = int(N)
while n != N:
    res += int(n)
    n = n[-1] + n[:-1]
print(res)