res = 0
cur = 'A'
for i in input():
    res += min(abs(ord(i) - ord(cur)), 26 - abs(ord(i) - ord(cur)))
    cur = i
print(res)