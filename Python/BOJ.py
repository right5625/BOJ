n = int(input())
if n < 3:
    print(1)
else:
    prev2, prev1 = 0, 1
    for i in range(n - 2):
        temp = prev2 + prev1
        prev2 = prev1
        prev1 = temp
    print(prev2 + prev1)