for i in range(int(input())):
    N = int(input())
    H = list(map(int, input().split()))
    res = 0
    for j in range(1, N - 1):
        if H[j] > H[j - 1] and H[j] > H[j + 1]:
            res +=1
    print(f'Case #{i + 1}: {res}')