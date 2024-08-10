from collections import defaultdict

codeDic = {'L' : 120, 'S' : 150, 'B' : 150, 'N' : 40, 'C' : 160, 'D' : 100, 'R' : 100, 'O' : 100}
while True:
    name = input()
    if name == '#':
        break
    dic = defaultdict(int)
    upgrade = 0
    while True:
        line = input()
        if line == '00A':
            break
        seat, code = line.split()
        try:
            dic[seat] += codeDic[code]
            if dic[seat] >= 200:
                upgrade += 1
        except:
            pass
    print(f'{name} {upgrade}')