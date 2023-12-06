M, K = map(int, input().split())
S = sum(list(map(int, input().split())))
print(S // M if S % M == 0 else S // M + 1)