for _ in range(int(input())):
    A, B = input().split()
    print(bin(int(A, 2) + int(B, 2))[2:])