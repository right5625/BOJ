K = int(input())
S = input()
for i in list(zip(*[S[K * i : K * (i + 1)] if i % 2 == 0 else S[K * i : K * (i + 1)][::-1] for i in range(len(S) // K)])):
    print(*i, sep = '', end = '')