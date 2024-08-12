import sys
input = lambda : sys.stdin.readline().rstrip()

flag = True
prevA = prevB = 0
for i in range(int(input())):
    A, B = map(int, input().split())
    if abs(A - B) % 12 == 7 and abs(prevA - prevB) % 12 == 7 and A != prevA and B != prevB:
        print(i)
        flag = False
    prevA, prevB = A, B
if flag:
    print('POLE')