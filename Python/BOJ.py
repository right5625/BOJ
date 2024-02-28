N = int(input())
res = 0
i = 1
while (N * i + i) % N != 0:
    res += N * i + i
    i += 1
print(res)