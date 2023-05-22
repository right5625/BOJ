N = int(input())
a = list(map(int, input().split()))[::-1]
for i in range(N):
    a[i] -= (i + 1)
print(max(a))