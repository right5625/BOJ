lst = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    lst.append(y)
print(abs(max(lst) - min(lst)))