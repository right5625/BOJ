a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
h, m, s = map(int, input().split())
t = h * b1 * c1 + m * c1 + s
print(t // (b2 * c2), t % (b2 * c2) // c2, t % c2)