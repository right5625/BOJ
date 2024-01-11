lst = []
for _ in range(8):
    t, rb = input().split()
    time = list(map(int, t.split(':')))
    lst.append([time[0] * 60000 + time[1] * 1000 + time[2], rb])
lst.sort()
score = [10, 8, 6, 5, 4, 3, 2, 1]
for i in range(8):
    lst[i] += [score[i]]
r = b = 0
for i in lst:
    if i[1] == 'R':
        r += i[2]
    else:
        b += i[2]
if r == b:
    print('Red' if lst[0][1] == 'R' else 'Blue')
else:
    print('Red' if r > b else 'Blue')