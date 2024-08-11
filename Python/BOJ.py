n = int(input())
print(1 if n == 0 else {1 : 2, 2 : 4, 3 : 8, 0 : 6}[n % 4])