print(sorted([list(input().split()) for _ in range(7)], key = lambda x : int(x[1]))[-1][0])