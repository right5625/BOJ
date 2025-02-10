<<<<<<< HEAD
def dfs(r, c, t):
    global res
    if r == c == N:
        res += 1
        return
    if t == 0:
        if not M[r][c + 1] and not vst[r][c + 1]:
            vst[r][c + 1] = True
            dfs(r, c + 1, 0)
            vst[r][c + 1] = False
            if not M[r + 1][c] and not vst[r + 1][c] and not M[r + 1][c + 1] and not vst[r + 1][c + 1]:
                vst[r + 1][c] = vst[r + 1][c + 1] = True
                dfs(r + 1, c + 1, 2)
                vst[r + 1][c] = vst[r + 1][c + 1] = False
    elif t == 1:
        if not M[r + 1][c] and not vst[r + 1][c]:
            vst[r + 1][c] = True
            dfs(r + 1, c, 1)
            vst[r + 1][c] = False
            if not M[r][c + 1] and not vst[r][c + 1] and not M[r + 1][c + 1] and not vst[r + 1][c + 1]:
                vst[r][c + 1] = vst[r + 1][c + 1] = True
                dfs(r + 1, c + 1, 2)
                vst[r][c + 1] = vst[r + 1][c + 1] = False
    else:
        if not M[r][c + 1] and not vst[r][c + 1]:
            vst[r][c + 1] = True
            dfs(r, c + 1, 0)
            vst[r][c + 1] = False
            if not M[r + 1][c] and not vst[r + 1][c] and not M[r + 1][c + 1] and not vst[r + 1][c + 1]:
                vst[r + 1][c] = vst[r + 1][c + 1] = True
                dfs(r + 1, c + 1, 2)
                vst[r + 1][c] = vst[r + 1][c + 1] = False
        if not M[r + 1][c] and not vst[r + 1][c]:
            vst[r + 1][c] = True
            dfs(r + 1, c, 1)
            vst[r + 1][c] = False

N = int(input())
M = [[1] * (N + 2)]
for _ in range(N):
    M.append([1] + list(map(int, input().split())) + [1])
M.append([1] * (N + 2))
vst = [[False for _ in range(N + 1)] for _ in range(N + 1)]
vst[1][1] = vst[1][2] = True
res = 0
dfs(1, 2, 0)
print(res)
=======
import sys, string
input = lambda: sys.stdin.readline().rstrip()

s = string.digits + string.ascii_lowercase
def convert(n, b):
    q, r = divmod(n, b)
    return s[r] if q == 0 else convert(q, b) + s[r]

for _ in range(int(input())):
    K, b, n = map(int, input().split())
    print(K, sum(s.index(i) ** 2 for i in convert(n, b)))
>>>>>>> 4fc83c260c222b8485c24defca145ab85a6354ec
