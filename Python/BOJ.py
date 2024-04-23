for _ in range(int(input())):
    s, n = input().split()
    print(f'Shifting {s} by {int(n)} positions gives us: {s[-int(n):] + s[:-int(n)]}')