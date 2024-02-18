lst = [0]
idx = 0
n = 1
while idx < 1001:
    for i in [n] * n:
        lst.append(i)
        idx += 1
    n += 1
A, B = map(int, input().split())
print(sum(lst[A : B + 1]))