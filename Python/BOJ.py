A = list(map(int, input().split()))
B = list(map(int, input().split()))
n, d = 0, 36
for i in A:
    for j in B:
        if i > j:
            n += 1
        elif i == j:
            d -= 1
print(f'{n / d:.5f}')