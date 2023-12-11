from collections import Counter

N, M = map(int, input().split())
print(max(Counter(list(map(int, input().split()))).values()))