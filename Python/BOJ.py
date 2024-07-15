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