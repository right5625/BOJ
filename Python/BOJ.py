w, h = map(int, input().split())
n, a, b = map(int, input().split())
print(-1) if w < a or h < b else print(n // ((w // a) * (h // b)) if n // ((w // a) * (h // b)) == n / ((w // a) * (h // b)) else n // ((w // a) * (h // b)) + 1)
