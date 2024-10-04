import re

c = 1
while True:
    a, b = input().split()
    if a == b == "#":
        break
    print(f"Case {c}")
    for _ in range(int(input())):
        print(re.sub(rf"[{a + b + a.upper() + b.upper()}]", "_", input()))
    print()
    c += 1
