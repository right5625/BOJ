for _ in range(int(input())):
    n = input()
    if n[len(n) - 1] == '!':
        n = n.rstrip('!')[:-1] + '1'
    print(0 if n.count('!') % 2 == 0 else 1) if n[-1] == '0' else print(1 if n.count('!') % 2 == 0 else 0)