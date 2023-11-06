h, w = map(int, input().split())
cnt = 0
for i in list(input() for _ in range(h)):
    cnt += i.count('0')
print(min(cnt, h * w - cnt))