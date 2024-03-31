mx, res = 0, ''
for i in [list(input().split()) for _ in range(int(input()))]:
    if i[2] == 'Russia' and mx < int(i[0]):
        res = i[1]
        mx = int(i[0])
print(res)