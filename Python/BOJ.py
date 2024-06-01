import sys
input = lambda : sys.stdin.readline().rstrip()

face = [[0, 1, 2, 3], [0, 1, 4, 5], [0, 2, 4, 6], [1, 3, 5, 7], [2, 3, 6, 7], [4, 5, 6, 7]]
for _ in range(int(input())):
    print('YES' if sorted(list(map(int, input().split()))) in face else 'NO')