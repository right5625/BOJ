for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print('Inner circle line' if b - a < 22 else 'Outer circle line')
    else:
        print('Outer circle line' if a - b < 22 else 'Inner circle line')