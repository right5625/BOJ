import string

N = int(input())
res = ''
for i in input():
    if i in string.ascii_lowercase:
        res += chr(ord(i) - N + 26 if ord(i) - N < ord('a') else ord(i) - N)
        N = N + 1 if N < 25 else 1
    else:
        res += i
print(res)