N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(f'{sum(A)}\n{sum([A[i] for i in range(N) if not B[i]])}')