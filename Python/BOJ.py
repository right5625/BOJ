import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    N, C, K = map(int, input().split())
    if N == C == K == 0:
        break
    dic = {i : 0 for i in range(1, K + 1)}
    for _ in range(N):
        for i in list(map(int, input().split())):
            dic[i] += 1
    print(*list(map(lambda x : x[0], filter(lambda x : x[1] == min(dic.values()), sorted(dic.items(), key = lambda x : (x[1], x[0]))))))