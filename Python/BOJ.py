A = list(map(int, input().split()))
while A != sorted(A):
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            print(*A)