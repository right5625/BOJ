import sys
input = lambda : sys.stdin.readline().rstrip()

card = {i : 0 for i in ['STRAWBERRY', 'BANANA', 'LIME', 'PLUM']}
for _ in range(int(input())):
    S, X = input().split()
    card[S] += int(X)
print('YES' if 5 in list(card.values()) else 'NO')