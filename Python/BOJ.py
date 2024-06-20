M, DM = map(int, input().split())
H, DH = map(int, input().split())
ML = [max(M - DM * i, 0) for i in range(100)]
HL = [max(H - DH * i, 0) for i in range(100)]
res = 0
for _ in range(int(input())):
    C, B = map(int, input().split())
    res += max(sum(ML[:C]), sum(HL[:B]))
print(res)