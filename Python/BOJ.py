lst = [int(input()) for _ in range(int(input()))]
res = 0
for i in set(lst):
    res = max(res, lst.count(i))
print(res)