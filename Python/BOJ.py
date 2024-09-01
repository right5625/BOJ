A, B = map(int, input().split())
cnt = 0
if A % 2 == 0:
    A += 1
    cnt += 1
if B % 2 == 1:
    B -= 1
    cnt += 1
print(cnt + (B - A + 1) // 2)
