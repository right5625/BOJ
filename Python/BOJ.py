n = int(input())
res = temp = 0
for i in list(map(int, input().split())):
    if i:
        temp += 1
    else:
        res = max(res, temp)
        temp = 0
print(max(res, temp))