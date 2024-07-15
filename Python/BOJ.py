<<<<<<< HEAD
import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    if not int(input()):
        break
    cur, res = 300, 0
    for i in list(map(int, input().split())):
        if cur >= i:
            cur -= i
            res += i
    print(res)
=======
print(min(int(input()) * 100, int(input()) * 100) // 2)
>>>>>>> 9c354e441cb17a752344603179e9c26d2d83822c
