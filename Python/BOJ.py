from collections import defaultdict

n, m, k, a, b, c = map(int, input().split())
dic = defaultdict(list)
for i, j in zip([n * a, m * b, k * c], ['Joffrey', 'Robb', 'Stannis']):
    dic[i].append(j)
print(*dic[max(dic)])