n = int(input())
a = list(input().split())
for i in range(n):
    for j in range(n):
        for k in range(1, min(len(a[i]), len(a[j])) + 1):
            if a[i][:k] == a[j][-k:]:
                print(i + 1, j + 1)
                exit()
print(-1)