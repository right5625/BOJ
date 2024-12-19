S = '001'
for _ in range(15):
    S += '0' + S[:len(S) // 2] + '1' + S[len(S) // 2 + 1:]
for c in range(int(input())):
    print(f'Case #{c + 1}: {S[int(input()) - 1]}')