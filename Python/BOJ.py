N = int(input())
A = list(map(int, input().split()))
print(min(A[:A.index(-1)]) + min(A[A.index(-1) + 1:]))