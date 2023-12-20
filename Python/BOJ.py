for _ in range(int(input())):
    print(*[i for i in list(map(int, input().split(', '))) if i % 4 == 0])