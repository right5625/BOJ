n = int(input())
s = input()
if len(s) > n:
    print('Impossible')
else:
    res = 0
    for i in s:
        res += ord(i) - 96
    print(res)