while True:
    K, J, T, D = map(int, input().split())
    if K == J == T == D == 0:
        break
    print('yes' if K + 0.5 > max(J - 0.5, 0) * 9 + max(T - 0.5, 0) * 4 + max(D - 0.5, 0) * 4 and max(K - 0.5, 0) < (J + 0.5) * 9 + (T + 0.5) * 4 + (D + 0.5) * 4 else 'no')