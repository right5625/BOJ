A = int(input())
B = int(input())
C = int(input())
S = str(A * B * C)
for i in range(10):
    print(S.count(str(i)))