n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())
i = 0
j = n - 1
cnt = 0
while i < j:
    if a[i] + a[j] > x:
        j -= 1
    elif a[i] + a[j] < x:
        i += 1
    else:
        cnt += 1
        j -= 1
print(cnt)