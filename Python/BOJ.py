from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
D = defaultdict(bool)
for i in A:
    D[i] = True
res = 'No'
for i in A:
    if D[i] and D[i + 3] and D[i + 6]:
        res = 'Yes'
        break
print(res)