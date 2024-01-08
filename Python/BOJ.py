N = int(input())
s = input()
res = 1
for i in 'yuiophjklbnm':
    if i == s[-1]:
        res = 0
        break
print(res)