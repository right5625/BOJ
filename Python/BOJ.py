for _ in range(int(input())):
    A = list(map(int, input().split()))
    for i in range(19, 0, -1):
        if A[i] >= 2:
            A[i - 1] += A[i] // 2
        A[i] = A[i] % 2
    print(*A)
