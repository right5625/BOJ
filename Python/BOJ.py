import sys
input = lambda : sys.stdin.readline().rstrip()

dic = {'M' : [0, 0], 'J' : [0, 0]}
for _ in range(int(input())):
    MJ, P = input().split()
    dic[MJ][0] += int(P)
    dic[MJ][1] += 1
avg1, avg2 = 0 if dic['M'][0] == 0 else dic['M'][0] / dic['M'][1], 0 if dic['J'][0] == 0 else dic['J'][0] / dic['J'][1]
print('V') if avg1 == avg2 else print('M' if avg1 > avg2 else 'J')