A, B, C = map(int, input().split())
I, J, K = map(int, input().split())
M = min(A / I, B / J, C / K)
print(A - I * M, B - J * M, C - K * M)