A = int(input())
inc, res = 1, 0
for _ in range(A):
    res = (res + inc) % 500000009
    inc = inc * 4 % 500000009
print(res)
