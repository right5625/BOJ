m1 = [tuple(map(int, input().split())) for _ in range(4)]
m2 = list(zip(*m1))
cnt = set()
for i in m1 + m2:
    cnt.add(sum(i))
print('magic' if len(cnt) == 1 else 'not magic')