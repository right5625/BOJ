from collections import deque

s = input()
q = deque()
q.append((s, 0))
res = 0
while q:
    t, n = q.popleft()
    if t[0] == t[-1]:
        res = n
        break
    q.append((s[1:], n + 1))
    q.append((s[:-1], n + 1))
print('Win' if res % 2 == 1 else 'Lose')