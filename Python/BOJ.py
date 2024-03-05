n = int(input())
print(777 if sum([list(map(int, input().split())) for _ in range(3)], []).count(7) == 3 else 0)