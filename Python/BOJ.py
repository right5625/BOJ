N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum((i + j) * max(i, j) for i in A for j in B))