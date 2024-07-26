for _ in range(int(input())):
    x = list(map(int, input().split()))
    print(f'The sequence {x[1:]} is not an arithmetic sequence.' if x[0] == 1 or len(set([x[i] - x[i - 1] for i in range(2, x[0] + 1)])) != 1 else f'The next 5 numbers after {x[1:]} are: {[i for i in range(x[-1] + (x[-1] - x[-2]), x[-1] + (x[-1] - x[-2]) * 6, x[-1] - x[-2])]}')