for _ in range(int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(min([abs(i - j) for i in A[1:] for j in B[1:]]))
