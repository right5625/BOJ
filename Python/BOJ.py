N = int(input())
a = list(map(int, input().split()))
x = 9001
for i in range(N):
    for j in range(i + 1, N):
        x = min(a[j] - a[i], x)
print("yes" if x >= 0 else "no")
