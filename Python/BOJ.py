w = input()
cnt = 0
for i in set(w):
    if w.count(i) % 2 == 1:
        cnt += 1
print(max(cnt - 1, 0))
