N = int(input())
a = []
while len(a) < N:
    a += list(map(int, input().split()))
res = temp = 0
for i in sorted(a)[::-1]:
    if i % 2 == 0:
        res += i
    else:
        if temp % 2 == 1:
            res += (i + temp)
            temp = 0
        else:
            temp = i
print(res // 2)