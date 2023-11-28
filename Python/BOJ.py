N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
new = [B[i] for i in range(N) if not A[i]][::-1]
print(*(new + C[:M - len(new)])) if len(new) < M else print(*new[:M])