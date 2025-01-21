b = int(input())
result = 'Nothing'
for k, v in {i: j for i, j in zip(['Watermelon', 'Pomegranates', 'Nuts'], [int(input()) for _ in range(3)])}.items():
    if b >= v:
        result = k
        break
print(result)