n = int(input())
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
f = s = 0
for i in d1:
    for j in d2:
        if i > j:
            f += 1
        elif i < j:
            s += 1
print('tie') if f == s else print('first' if f > s else 'second')