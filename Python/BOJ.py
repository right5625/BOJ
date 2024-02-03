n, a, b = map(int, input().split())
w = [int(input()) for _ in range(n - 1)]
if a not in w and b not in w:
    print(-1)
elif a not in w:
    print(a)
elif b not in w:
    print(b)
else:
    for i in range(a, b + 1):
        print(i)