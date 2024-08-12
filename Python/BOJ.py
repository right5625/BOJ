import sys
input = lambda : sys.stdin.readline().rstrip()

res = []
prevA = prevB = 0
for i in range(int(input())):
    A, B = map(int, input().split())
    if abs(A - B) % 12 == abs(prevA - prevB) % 12 == 7 and A != prevA and B != prevB:
        res.append(i)
    prevA, prevB = A, B
print(*res, sep = '\n') if res else print('POLE')