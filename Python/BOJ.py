import sys
input = lambda : sys.stdin.readline().rstrip()

def round_2(val, digits):
    return round(val + 10 ** (-len(str(val)) - 1), digits)

for _ in range(int(input())):
    S = list(map(int, input().split()))
    print(f'{round_2(len(list(filter(lambda x : x > sum(S[1:]) / S[0], S[1:]))) / S[0] * 100, 3):.3f}%')