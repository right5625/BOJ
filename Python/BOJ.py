import math

n = int(input())
print(sum(math.ceil(i / 2) for i in list(map(int, input().split()))))