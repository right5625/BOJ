N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = b = res = 0
for i in range(N):
    a += A[i]
    b += B[i]
    if a == b:
        res = i + 1
print(res)