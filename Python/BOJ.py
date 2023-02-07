import math

N = int(input())
prime = [True] * (N + 1)
prime[0] = prime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if prime[i]:
        for j in range(i * 2, N + 1, i):
            prime[j] = False
res = []
while N > 1:
    for i in range(2, N + 1):
        if prime[i] and N % i == 0:
            res.append(i)
            N //= i
if res:
    print(*sorted(res), sep = '\n')