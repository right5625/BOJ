while True:
    n, f = input().split()
    if n == '#':
        break
    print(f'{n} Library')
    for i in range(int(input())):
        w, s = input().split()
        print(f'Book {i + 1} {"horizontal" if int(w) >= int(f) * len(s) + 2 else "vertical"}')