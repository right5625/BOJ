for _ in range(int(input())):
    N = int(input())
    S = input()
    K = (ord(input()) - ord(S[0]) + 26) % 26
    print(''.join([chr((ord(i) - ord('a') + K) % 26 + ord('a')) for i in S]))