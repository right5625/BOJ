while True:
    D, N = input().split()
    if D == N == '0':
        break
    try:
        print(int(N.replace(D, '')))
    except:
        print(0)