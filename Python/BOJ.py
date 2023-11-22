N = int(input())
A = [input() for _ in range(N)]
for i in range(1, N):
    if A[i] == 'Present!':
        A[i - 1] = A[i] = False
if len(A) == A.count(False):
    print('No Absences')
else:
    for i in A:
        if i:
            print(i)