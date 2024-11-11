N = int(input())
A = list(map(int, input().split()))
res = [1 if A[0] else -1]
for i in A[1:]:
    res.append(res[-1] + 1 if i else res[-1] - 1)
print(sum(res))
