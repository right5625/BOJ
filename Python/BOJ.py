N, K = map(int, input().split())
dic = {i: [] for i in 'srp'}
for i in input():
    if len(dic[i]) < K:
        dic[i].append(i)
    else:
        if i == 's':
            if len(dic['r']) < K:
                dic['r'].append(i)
            else:
                dic['p'].append(i)
        elif i == 'r':
            if len(dic['p']) < K:
                dic['p'].append(i)
            else:
                dic['s'].append(i)
        else:
            if len(dic['s']) < K:
                dic['s'].append(i)
            else:
                dic['r'].append(i)
for i in dic.values():
    print(''.join(i))