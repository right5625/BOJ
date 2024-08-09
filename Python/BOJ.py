A = list(map(int, input().split()))
N, K = map(int, input().split())
print(sum([A[i] * A[i + 1] for i in range(0, 10, 2)]) // 5 * N // K)