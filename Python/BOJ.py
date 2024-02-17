def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

N = list(map(int, input().split()))
print(min([(N[i] * N[j] // gcd(N[i], N[j]) * N[k]) // gcd(N[i] * N[j] // gcd(N[i], N[j]), N[k]) for i in range(5) for j in range(i + 1, 5) for k in range(j + 1, 5)]))