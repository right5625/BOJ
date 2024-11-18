lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
res1, res2 = 0, 1.5
for i, j in zip(range(6), [13, 7, 5, 3, 3, 2]):
    res1 += lst1[i] * j
    res2 += lst2[i] * j
print("cocjr0208" if res1 > res2 else "ekwoo")
