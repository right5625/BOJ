import re

moves = {
    'N' : lambda n : (0, n),
    'NE' : lambda n : ((n * n / 2) ** 0.5, (n * n / 2) ** 0.5),
    'E' : lambda n : (n, 0),
    'SE' : lambda n : ((n * n / 2) ** 0.5, -(n * n / 2) ** 0.5),
    'S' : lambda n : (0, -n),
    'SW' : lambda n : (-(n * n / 2) ** 0.5, -(n * n / 2) ** 0.5),
    'W' : lambda n : (-n, 0),
    'NW' : lambda n : (-(n * n / 2) ** 0.5, (n * n / 2) ** 0.5)
}

while True:
    S = list(input().replace('.', '').split(','))
    if S[0] == 'END':
        break
    cur = [0, 0]
    for i in S:
        n, d = re.match(r'(\d+)([NESW]+)', i).groups()
        move = moves[d](int(n))
        cur[0] += move[0]
        cur[1] += move[1]
    print(f'You can go to ({cur[0]:.3f},{cur[1]:.3f}), the distance is {(cur[0] ** 2 + cur[1] ** 2) ** 0.5:.3f} steps.')