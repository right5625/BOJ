import string

n, A, B = input().split()
r = s = 0
for i in range(int(n)):
    if A[i] == B[i]:
        r += 1
for i in string.ascii_uppercase:
    if i in A and i in B:
        s += min(A.count(i), B.count(i))
print(r, s - r)