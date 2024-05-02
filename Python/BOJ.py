prev2, prev1, res = 0, 1, 1
for _ in range(1, int(input())):
    res = prev2 + prev1
    prev2 = prev1
    prev1 = res
print(res)