import math

def func():
    while True:
        res = 0
        while True:
            S = list(input().split())
            if S[0] == '0':
                print(res)
                break
            elif S[0] == '#':
                return
            else:
                if S[3] == 'F':
                    res += int(S[2]) * 2
                elif S[3] == 'B':
                    res += math.ceil(int(S[2]) * 1.5)
                else:
                    res += max(int(S[2]), 500)

func()