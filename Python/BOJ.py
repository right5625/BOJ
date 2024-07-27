n = int(input())
a = list(map(int, input().split()))
print(max(abs(a.index(0) - (n - 1 - a[::-1].index(1))), abs(a.index(1) - (n - 1 - a[::-1].index(0)))))