N = int(input())
res = 1
prev = temp = 0
for i in list(map(int, input().split())):
    if prev <= i:
        temp += 1
    else:
        res = max(res, temp)
        temp = 1
    prev = i
print(max(res, temp))