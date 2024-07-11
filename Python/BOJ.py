A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) == sum(B):
    res = 'remis'
    for i in range(10, -1, -1):
        if A.count(i) > B.count(i):
            res = 'Algosia'
            break
        elif A.count(i) < B.count(i):
            res = 'Bajtek'
            break
    print(res)
else:
    print('Algosia' if sum(A) > sum(B) else 'Bajtek')