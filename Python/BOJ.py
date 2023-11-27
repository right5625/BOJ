N = int(input())
S = list(map(int, input().split()))
T, P = map(int, input().split())
res = 0
for i in S:
    res += i // T if i % T == 0 else i // T + 1
s = sum(S)
print(f'{res}\n{s // P} {s % P}')