res = 0
for _ in range(int(input())):
    T = list(map(int, input().split()))
    if (T.count(-1) in [1, 2] and len(T[:T.index(-1)]) + T.count(-1) == 3 and T[:T.index(-1)] == sorted(T[:T.index(-1)])) or (-1 not in T and T == sorted(T)):
        res += 1
print(res)