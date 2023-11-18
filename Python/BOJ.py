N = int(input())
M = input()
K = int(input())
print(K - 1 if K % 2 == 0 else K) if M == 'annyong' else print(K - 1 if K != 1 else K + 1) if K % 2 == 1 else print(K)