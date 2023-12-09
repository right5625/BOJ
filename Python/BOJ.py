seat = {chr(i) : ['.'] * 20 for i in range(ord('A'), ord('J') + 1)}
for _ in range(int(input())):
    S = input()
    seat[S[0]][int(S[1:]) - 1] = 'o'
for i in seat.values():
    print(*i, sep = '')