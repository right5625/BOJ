lst = [[4, 7]]
while len(str(lst[-1][0])) < 6:
    lst.append([int(i + str(j)) for i in '47' for j in lst[-1]])
N = int(input())
lst = sum(lst, [])
res = 0
for i in range(len(lst)):
    if lst[i] > N:
        res = lst[i - 1]
        break
print(res if res != 0 else lst[-1])