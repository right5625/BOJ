N, M = map(int, input().split())
time, res = [0] * N, [0] * N
for _ in range(M):
    s = list(map(int, input().split()))
    t, v, z = s[0], s[1], s[2:]
    for i in sorted(z):
        idx = z.index(i)
        if t >= time[idx]:
            res[idx] += v
            time[idx] = t + i
            break
print(*res)