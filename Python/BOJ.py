K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
res = 0
for i in A:
    for j in B:
        if j - i == K:
            res += 1
print(res)