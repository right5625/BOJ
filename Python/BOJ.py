m = [int(input()) for _ in range(int(input()))]
if 3 in m:
    print('None')
elif m.count(5) == len(m):
    print('Named')
elif sum(m) / len(m) >= 4.5:
    print('High')
else:
    print('Common')