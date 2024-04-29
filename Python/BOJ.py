dic = {i : 0 for i in 'lkp'}
for _ in range(3):
    try:
        dic[input()[0]] += 1
    except:
        pass
print('GLOBAL' if list(dic.values()).count(1) == 3 else 'PONIX')