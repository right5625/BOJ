m = int(input())
n = int(input())
res = 0
for i in range(1, m + 1):
    for j in range(n, 0, -1):
        if i + j == 10:
            res += 1
            break
print('There is 1 way to get the sum 10.' if res == 1 else f'There are {res} ways to get the sum 10.')