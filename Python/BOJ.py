N = int(input())
A = list(map(int, input().split()))
cur = A[0]
res = 1
for i in A[1:]:
    if (cur % 2 == 0 and i % 2 == 1) or (cur % 2 == 1 and i % 2 == 0):
        cur = i
        res += 1
print(res)