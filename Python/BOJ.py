for _ in range(int(input())):
    a, b = map(set, input().split())
    print("YES" if a == b else "NO")
