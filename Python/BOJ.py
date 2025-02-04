import string

N = int(input())
<<<<<<< HEAD
X = int(input())
res = 0
for _ in range(N):
    P = list(map(int, input().split()))
    if abs(P[0] - P[1]) <= X:
        res += max(P[0], P[1])
    else:
        P3 = int(input())
        res += P3
=======
res = ''
for i in input():
    if i in string.ascii_lowercase:
        res += chr(ord(i) - N + 26 if ord(i) - N < ord('a') else ord(i) - N)
        N = N + 1 if N < 25 else 1
    else:
        res += i
>>>>>>> 9bfdac18b00e3867bb88931196da0948e4b1edd5
print(res)