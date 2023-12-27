input()
dic = {i : 0 for i in 'roygbivROYGBIV'}
for i in input():
    if i in 'roygbivROYGBIV':
        dic[i] = 1
res1 = sum(list(dic[i] for i in 'roygbiv'))
res2 = sum(list(dic[i] for i in 'ROYGBIV'))
if res1 == 7 and res2 == 7:
    print('YeS')
elif res1 == 7:
    print('yes')
elif res2 == 7:
    print('YES')
else:
    print('NO!')