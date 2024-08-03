N, K, M = map(int, input().split())
G = [list(map(int, input().split()))[1:] for _ in range(K)]
C = list(map(int, input().split()))
print(sum([-(-sum(C[j - 1] for j in i) // M) for i in G]))