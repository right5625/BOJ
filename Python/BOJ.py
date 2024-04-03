Cu, Du = map(int, input().split())
Cd, Dd = map(int, input().split())
Cp, Dp = map(int, input().split())
H = int(input())
res = 0
while True:
    if res % Cu == 0:
        H -= Du
    if res % Cd == 0:
        H -= Dd
    if res % Cp == 0:
        H -= Dp
    if H <= 0:
        break
    res += 1
print(res)