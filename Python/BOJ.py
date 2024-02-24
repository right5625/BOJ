N, K = map(int, input().split())
A = list(map(int, input().split(',')))
for i in range(K):
    A = [A[j + 1] - A[j] for j in range(N - (i + 1))]
print(*A, sep = ',')