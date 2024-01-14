import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
lst = [0]
cnt = 0
for i in [list(map(int, input().split())) for _ in range(N)]:
    if i[0] < i[1]:
        lst.append(i[1] - i[0])
    else:
        cnt += 1
lst.sort()
print(lst[max(K - cnt, 0)])