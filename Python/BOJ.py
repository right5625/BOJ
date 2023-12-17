dic = {'B' : 0, 'S' : 0, 'A' : 0}
N = int(input())
for i in input():
    dic[i] += 1
if dic['B'] == dic['S'] == dic['A']:
    print('SCU')
else:
    for k, v in dic.items():
        if v == max(dic.values()):
            print(k, end = '')