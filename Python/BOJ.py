n = int(input())
a = list(map(int, input().split()))
DP = [1] * n
for i in range(1, n):
    DP[i] = DP[i - 1] + 1 if a[i - 1] < a[i] else 1
print(max(DP))