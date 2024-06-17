import string
from collections import defaultdict

A = input()
B = ''.join([i for i in input() if i in string.ascii_uppercase])
print(*[chr(ord(B[i]) + (ord(A[i % len(A)]) - ord('A')) - 26) if chr(ord(B[i]) + (ord(A[i % len(A)]) - ord('A'))) > 'Z' else chr(ord(B[i]) + (ord(A[i % len(A)]) - ord('A'))) for i in range(len(B))], sep = '')