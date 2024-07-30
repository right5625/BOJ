N = int(input())
A = list(map(int, input().split()))
lst = list(map(lambda x : min(x), [[abs(N - (i * (N // i))), abs(N - (i * (N // i + 1)))] for i in A]))
print(f'{A[lst.index(min(lst))]} {N - min(lst) if (N - min(lst)) % A[lst.index(min(lst))] == 0 else N + min(lst)}')