for _ in range(int(input())):
    N = input()
    print('Good' if (int(N) + 1) % int(N[2:]) == 0 else 'Bye')