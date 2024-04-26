N = int(input())
A = list(map(int, input().split()))
for i in range(len(A)):
    if A[i] == max(A):
        print(chr(65 + i), end = '')