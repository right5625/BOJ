N = int(input())
A = input()
B = input()
res = [0, 0]
for i, j in zip(A, B):
    if i == 'R':
        if j == 'S':
            res[0] += 1
        elif j == 'P':
            res[1] += 1
    elif i == 'S':
        if j == 'R':
            res[1] += 1
        elif j == 'P':
            res[0] += 1
    else:
        if j == 'R':
            res[0] += 1
        elif j == 'S':
            res[1] += 1
print(*res)