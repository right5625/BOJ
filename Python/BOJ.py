x, y = map(int, input().split())
day = y
for i in range(1, x):
    if i == 2:
        day += 28
    elif i in [4, 6, 9, 11]:
        day += 30
    else:
        day += 31
print(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][day % 7])