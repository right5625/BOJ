N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())
print(int(N * X // 100), len(list(filter(lambda n : n >= Y, A))))