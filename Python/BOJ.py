n = int(input())
dic = {str(i) + j : 0 for i in range(1, 6) for j in ['A', 'B', 'C']}
for i in list(input().split()):
    dic[i] += 1
flag = True
for i in range(1, 5):
    for j in ['A', 'B', 'C']:
        if not dic[str(i) + j]:
            flag = False
for i in ['5A', '5B', '5C']:
    if dic[i] < 2:
        flag = False
print('TAK' if flag else 'NIE')