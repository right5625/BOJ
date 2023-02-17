N = int(input())
DP = [i for i in range(N + 1)]
for i in range(4, N + 1):
    DP[i] = (DP[i - 1] + DP[i - 2]) % 15746
print(DP[N])