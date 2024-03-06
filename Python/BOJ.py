n = input()
res = -1
t = ''
for i in range(1, 11):
    t += str(i)
    if n == t:
        res = i
        break
print(res)