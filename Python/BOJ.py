A = input()
B = input()
C = 'ABCDE'
P = ''
for i in range(0, 10, 2):
    temp = A[i : i + 2] + B[i : i + 2]
    if temp.count(C[i // 2]) == 0:
        P += C[i // 2].lower()
    elif temp.count(C[i // 2]) == 1 or temp.count(C[i // 2] + C[i // 2].lower()) == 2:
        P += C[i // 2] + C[i // 2].lower()
    else:
        P += C[i // 2]
for _ in range(int(input())):
    flag = True
    for i in input():
        if i not in P:
            flag = False
            break
    print('Possible baby.' if flag else 'Not their baby!')