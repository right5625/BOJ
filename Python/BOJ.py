for _ in range(int(input())):
    print("YES" if sum(list(map(int, input()))) % 9 == 0 else "NO")
