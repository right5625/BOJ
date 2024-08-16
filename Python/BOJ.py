n = int(input())
print('TAK' if set(list(map(int, input().split()))) == set(range(1, n + 1)) else 'NIE')